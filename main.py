from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from typing import Optional
from service.request_data import get_all_urls
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def root():
  return {"message": "Is working!"}

class Item(BaseModel):
    reads: str
    vcf: str
    catalog: Optional[str] = None
    locus: str

@app.post('/reviewer', response_class=PlainTextResponse)
async def create_task(item: Item):
    # # parse path of files to use with REViewer
    request_data = item.dict()
    urls = [
      # request_data.get('reads', ''),
      # request_data.get('vcf', ''),
      request_data.get('catalog', '')
      # request_data.get('locus')
    ]

    # # TODO: get files from remote
    # # TODO: store files from remote
    # # TODO: run REViewer with local file path as arguments
    # # TODO: send back REViewer generated SVG

    results = await get_all_urls(urls)

    # print(results)

    # with open("./tmp_data/test.txt", "w") as fo:
    #    fo.write("This is Test Data")

    return f'''<svg
      version="1.1"
       baseProfile="full"
       width="800" height="100"
       xmlns="http://www.w3.org/2000/svg">

      <rect width="100%" height="100%" fill="red" />
      <text x="20" y="30" font-size="20" fill="black">
        Reads: {request_data.get('reads', '')}
      </text>
      <text x="20" y="50" font-size="20" fill="black">
        VCF: {request_data.get('vcf', '')}
      </text>
      <text x="20" y="70" font-size="20" fill="black">
        Catalog: {request_data.get('catalog', '')}
      </text>
      <text x="20" y="90" font-size="20" fill="black">
        Locus: {request_data.get('locus', '')}
      </text>
    </svg>'''

