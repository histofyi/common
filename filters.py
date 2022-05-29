

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


def structure_title(structure, short=False):
    title = None
    if 'complex' in structure:
        print ('has complex')
        if 'slug' in structure['complex']:
            print ('has slug')
            print (structure['complex']['slug'])
            if structure["allele"] is None:
                if structure['organism'] is not None:
                    allele = structure['organism']['common_name'].capitalize() + ' MHC Class I'
            else:
                allele = class_i_display_name(structure["allele"]["mhc_alpha"])
            if structure['complex']['slug'] == 'class_i_with_peptide':
                title = f'{allele} binding {structure["peptide"]["sequence"]} at {structure["resolution"]}&#8491; resolution'
            if structure['complex']['slug'] == 'class_i_with_tapbpr':
                title = f'{allele} binding TAPBR at {structure["resolution"]}&#8491; resolution'
            if structure['complex']['slug'] == 'class_i_possibly_without_peptide':
                title = f'{allele} with no distinct peptide at {structure["resolution"]}&#8491; resolution'
            if structure['complex']['slug'] == 'class_i_with_peptide_and_ly49c':
                title = f'{allele} with {structure["peptide"]["sequence"]} and Ly49c NK receptor at {structure["resolution"]}&#8491; resolution'
            if structure['complex']['slug'] == 'class_i_with_peptide_and_kir':
                title = f'{allele} with {structure["peptide"]["sequence"]} and KIR NK receptor at {structure["resolution"]}&#8491; resolution'
            if structure['complex']['slug'] == 'class_i_with_peptide_and_lir2':
                title = f'{allele} with {structure["peptide"]["sequence"]} and LIR-2 at {structure["resolution"]}&#8491; resolution'
            if structure['complex']['slug'] == 'class_i_with_peptide_and_lir1':
                title = f'{allele} with {structure["peptide"]["sequence"]} and LIR-1 at {structure["resolution"]}&#8491; resolution'
            if structure['complex']['slug'] == 'class_i_with_peptide_and_us2':
                title = f'{allele} with {structure["peptide"]["sequence"]} and human cytomegalovirus protein US2 at {structure["resolution"]}&#8491; resolution'
            if structure['complex']['slug'] == 'class_i_with_peptide_and_e3':
                title = f'{allele} with {structure["peptide"]["sequence"]} and human adenovirus protein E3 at {structure["resolution"]}&#8491; resolution'
            if structure['complex']['slug'] in ['class_i_with_peptide_and_alpha_beta_tcr', 'class_i_with_peptide_and_gamma_delta_tcr']:
                print ('is tcr')
                if 'alpha_beta' in structure['complex']['slug']:
                    tcr_type = 'Alpha/Beta'
                else:
                    tcr_type = 'Gamma/Delta'
                title = f'{allele} presenting {structure["peptide"]["sequence"]} to {tcr_type} T-cell receptor at {structure["resolution"]}&#8491; resolution'
            if structure['complex']['slug'] in ['class_i_with_peptide_and_cd8', 'class_i_with_peptide_and_cd8_dimer']:
                title = f'{allele} binding {structure["peptide"]["sequence"]} with CD8 at {structure["resolution"]}&#8491; resolution'
    if not title:
        if 'publication' in structure:
            title = f'"{structure["publication"]["citation"]["title"]}"'
        else:
            title = 'Currently unassigned'
    else:
        if not short:
            title = f'{title}<br /><small>Title : "{structure["publication"]["citation"]["title"]}"</small>'
    return title


def resolution_display(resolution):
    if resolution is not None:
        return f'{str(resolution)[:4]}&#8491;'
    else:
        return 'unknown'