from flask import current_app
from common.providers import s3Provider, awsKeyProvider


from common.helpers import fetch_constants, fetch_core, fetch_facet


def structure_view(pdb_code):
    blocks = ['chains', 'allele_match', 'aligned', 'peptide_matches', 'peptide_neighbours', 'peptide_structures', 'pockets', 'peptide_angles', 'cleft_angles', 'c_alpha_distances']
    message = 'This structure is of a non-classical Class I molecule or a homologue, or a classical Class I molecule with some issues in the underlying data. These structures will be available in a future release.'
    display = False
    structure, success, errors = fetch_core(pdb_code, current_app.config['AWS_CONFIG'])
    if 'complex' in structure:
        if 'components' in structure['complex']:
            if 'class_i_alpha' in structure['complex']['components']:
                display = True
                message = None
    associated_structures = {}
    if display:
        if success:
            structure['pdb_code'] = pdb_code
            structure['facets'] = {}
            for block in blocks:
                block_data, success, errors = fetch_facet(pdb_code, block, current_app.config['AWS_CONFIG'])
                structure['facets'][block] = block_data
            if structure['associated_structures'] is not None:
                for associated_structure in structure['associated_structures']:
                    thisstructure, success, errors = fetch_core(associated_structure, current_app.config['AWS_CONFIG'])
                    if success and associated_structure != pdb_code:
                        associated_structures[associated_structure] = thisstructure
    return {'structure':structure, 'pdb_code':pdb_code, 'features':fetch_constants('features'), 'chain_types':fetch_constants('chains'), 'associated_structures':associated_structures, 'display': display, 'message':message}
