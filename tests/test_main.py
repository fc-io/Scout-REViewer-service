from fastapi.testclient import TestClient

from main import app
from service.utils.get_root_path import get_root_path
from tests.test_data.example_svg import SVG

client = TestClient(app)

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Scout-REViewer-service is running!'}

def test_reviewer():
    """
      Test REViewer svg generation.
      This test uses file path and assumes that a reference file has been
      included in the project.
    """
    json = {
      # pylint: disable=line-too-long
      'reads': f'{get_root_path()}/tests/test_data/justhusky_exphun_hugelymodelbat_realigned.bam',
      'reads_index': f'{get_root_path()}/tests/test_data/justhusky_exphun_hugelymodelbat_realigned.bam.bai',
      # pylint: enable=line-too-long
      'vcf': f'{get_root_path()}/tests/test_data/justhusky_exphun_hugelymodelbat.vcf',
      'catalog': f'{get_root_path()}/tests/test_data/catalog_test.json',
      'locus': 'TCF4'
    }

    response = client.post(
        '/reviewer',
        json=json,
    )
    assert response.status_code == 200
    assert response.text == SVG
