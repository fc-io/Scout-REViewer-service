import os
import subprocess

from dotenv import dotenv_values
from service.utils.get_tmp_data_path import get_tmp_data_path

def generate_svg(data, file_id, files):
    env = dotenv_values('.env')
    path = get_tmp_data_path()
    output_prefix = f'{path}/{file_id}'

    # should really be no need to check output path here since we've already
    # created the folder when we stored the input files
    os.makedirs(path, exist_ok=True)
    locus = data.get('locus', '')

    cmd = [
      env.get('REV_PATH'),
      '--reads', files.get('reads', ''),
      '--vcf', files.get('vcf', ''),
      '--catalog', files.get('catalog') or env.get('REV_CATALOG_PATH'),
      '--locus', locus,
      '--reference', data.get('reference') or env.get('REV_REF_PATH'),
      '--output-prefix', output_prefix
    ]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)

    print('REViewer:')
    print(result.stdout.decode('utf-8'))

    return f'{output_prefix}.{locus}.svg'
