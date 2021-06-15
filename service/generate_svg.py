import os
import subprocess
import uuid

from service.utils.get_root_path import get_root_path
def generate_svg(data, file_id, files):
    root_path = get_root_path()
    path = f'{root_path}/tmp_data'
    output_prefix = f'{path}/{file_id}'

    # should really be no need to check output path here since we've already
    # created the folder when we stored the input files
    os.makedirs(path, exist_ok=True)

    locus = data.get('locus', '')

    cmd = [
      os.environ['REV_PATH'],
      '--reads', files.get('reads', ''),
      '--vcf', files.get('vcf', ''),
      '--catalog', files.get('catalog', f'{root_path}/data/catalog_test.json'),
      '--locus', locus,
      '--reference', data.get('reference', f'{root_path}/data/human_g1k_v37_decoy.fasta'),
      '--output-prefix', output_prefix
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)

    print('REViewer stdout >>> \n')
    print(result.stdout.decode('utf-8'))
    print('<<< REViewer stdout')

    return f'{output_prefix}.{locus}.svg'
