import subprocess
import uuid

def generate_svg(files):
    locus = request_data.get('locus', '')
    print(locus, files)

    # subprocess.check_output(['ls', '-l'])

    cmd = [
      # 'REViewer',
      '~/bin/REViewer/build/install/bin/REViewer',
      '--reads', request_data.get('reads', '')
      '--vcf', request_data.get('vcf', '')
      '--locus', request_data.get('locus', '')
      '--catalog', request_data.get('catalog', '')
      '--reference', request_data.get('reference', '')
      '--output-prefix'
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))

    return
