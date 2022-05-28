from flask import current_app
from common.providers import s3Provider, awsKeyProvider
from common.forms import request_variables

def structure_lookup():
    s3 = s3Provider(current_app.config['AWS_CONFIG'])
    variables = request_variables(None, ['pdb_code'])
    if variables['pdb_code'] is not None:
        pdb_code = variables['pdb_code'].lower()
        if '_' in pdb_code:
            pdb_code = pdb_code.split('_')[0]
        data, success, errors = s3.get(awsKeyProvider().block_key(pdb_code, 'core', 'info'))
    else:
        success = False
    if success:
        return {'redirect_to': f'/structures/view/{pdb_code}'}
    else:
        return {'variables': variables}
