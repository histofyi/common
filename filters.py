

def class_i_display_name(allele):
    if allele is not None:
        if 'h2-' in allele:
            display_name = f'{allele[0].upper()}{allele[1:3]}{allele[3].upper()}{allele[4:]}'
        elif ':' in allele:
            n = 2
            groups = allele.split(':')
            display_name = ':'.join(groups[:n])
        else:
            display_name = allele
        return display_name
    else:
        return 'Unmatched'


def structure_title(structure):
    title = ''
    if 'slug' in structure['complex']:
        if structure["allele"] is None:
            if structure['organism'] is not None:
                allele = structure['organism']['common_name'] + ' MHC Class I'
        else:
            allele = class_i_display_name(structure["allele"]["mhc_alpha"])
        if structure['complex']['slug'] == 'class_i_with_peptide':
            title = f'{allele} binding {structure["peptide"]["sequence"]} at {structure["resolution"]}&#8491; resolution'
        if structure['complex']['slug'] in ['class_i_with_peptide_and_alpha_beta_tcr', 'class_i_with_peptide_and_alpha_beta_tcr']:
            if 'alpha_beta' in structure['complex']['slug']:
                tcr_type = 'Alpha/Beta'
            else:
                tcr_type = 'Delta/Gamma'
            title = f'{allele} presenting {structure["peptide"]["sequence"]} to {tcr_type} T cell receptor at {structure["resolution"]}&#8491; resolution'

    else:
        title = f'Currently unassigned - "{structure["publication"]["citation"]["title"]}"'
    return title



def resolution_display(resolution):
    if resolution is not None:
        return f'{str(resolution)[:4]}&#8491;'
    else:
        return 'unknown'