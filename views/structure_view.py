from flask import current_app
from common.providers import s3Provider, awsKeyProvider

import doi

from common.helpers import fetch_constants, fetch_core


def structure_view(pdb_code):
    blocks = ['chains', 'allele_match', 'aligned', 'peptide_matches', 'peptide_neighbours', 'peptide_structures', 'peptide_angles', 'cleft_angles', 'c_alpha_distances']
    structure, success, errors = fetch_core(pdb_code, current_app.config['AWS_CONFIG'])
    associated_structures = {}
    if success:
        structure['pdb_code'] = pdb_code
        structure['facets'] = {}
        s3 = s3Provider(current_app.config['AWS_CONFIG'])
        for block in blocks:
            block_key = awsKeyProvider().block_key(pdb_code, block, 'info')
            block_data, success, errors = s3.get(block_key)
            structure['facets'][block] = block_data
        if structure['doi'] is not None:
            structure['doi_url'] = doi.get_real_url_from_doi(structure['doi'])
        if structure['associated_structures'] is not None:
            for associated_structure in structure['associated_structures']:
                thisstructure, success, errors = fetch_core(associated_structure, current_app.config['AWS_CONFIG'])
                if success and associated_structure != pdb_code:
                    associated_structures[associated_structure] = thisstructure
    return {'structure':structure, 'pdb_code':pdb_code, 'chain_types':fetch_constants('chains'), 'associated_structures':associated_structures}
