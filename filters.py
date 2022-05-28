

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
        if structure['complex']['slug'] == 'class_i_with_peptide':
            allele = class_i_display_name(structure["allele"]["mhc_alpha"])
            title = f'{allele} binding {structure["peptide"]["sequence"]} at {structure["resolution"]}&#8491; resolution'
    else:
        title = f'Currently unassigned - "{structure["publication"]["citation"]["title"]}"'
    return title



def resolution_display(resolution):
    if resolution is not None:
        return f'{str(resolution)[:4]}&#8491;'
    else:
        return 'unknown'