'''
    Test REViewer svg generation.

    Integration tests that test the whole stack:
      * The API
      * Data storage, retrieval and deletion.
      * Running the REViewer script with real data

    This test assumes a reference file (.fasta) in the .env file that you've
    added to the project. It also assumes a reference index file (.fasta.fai)
    accompanying the reference file. The reference index file (.fasta.fai) will
    be generated the first time you run the reference file (.fasta) through
    REViwer if you've not provided one.
'''
import os

from fastapi.testclient import TestClient
from dotenv import dotenv_values

from main import app
from service.utils.get_root_path import get_root_path
from tests.test_data.example_svg import SVG

client = TestClient(app)

env = dotenv_values('.env')

# pylint: disable=line-too-long, invalid-name
reads = f'{get_root_path()}/tests/test_data/justhusky_exphun_hugelymodelbat_realigned.bam'
reads_index = f'{get_root_path()}/tests/test_data/justhusky_exphun_hugelymodelbat_realigned.bam.bai'
vcf = f'{get_root_path()}/tests/test_data/justhusky_exphun_hugelymodelbat.vcf'
reference = env.get('REV_REF_PATH')
reference_index = f'{reference}.fai'
catalog = f'{get_root_path()}/tests/test_data/catalog_test.json'
locus = 'TCF4'
# pylint: enable=line-too-long

def test_files_has_data():
    assert os.path.getsize(reads) != 0
    assert os.path.getsize(reads_index) != 0
    assert os.path.getsize(vcf) != 0
    assert os.path.getsize(reference) != 0
    assert os.path.getsize(reference_index) != 0
    assert os.path.getsize(catalog) != 0

def test_root():
    res = client.get('/')
    assert res.status_code == 200
    assert res.json() == {'message': 'Scout-REViewer-service is running!'}

def test_path_api_with_no_optional_values():
    json = {
      'reads': reads,
      'reads_index': reads_index,
      'vcf': vcf,
      'locus': locus
    }

    res = client.post(
        '/reviewer',
        json=json,
    )
    assert res.status_code == 200
    assert res.text == SVG

def test_path_api_with_optional_values():
    json = {
      'reads': reads,
      'reads_index': reads_index,
      'vcf': vcf,
      'reference': reference,
      'reference_index': reference_index,
      'catalog': catalog,
      'locus': locus
    }

    res = client.post(
        '/reviewer',
        json=json,
    )
    assert res.status_code == 200
    assert res.text == SVG
