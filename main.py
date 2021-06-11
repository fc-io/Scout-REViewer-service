from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import Optional

from service.request_data import store_data

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Is working!"}

class Reviewer(BaseModel):
    reads: str
    vcf: str
    catalog: Optional[str] = None
    locus: str

@app.post('/reviewer', response_class=PlainTextResponse)
async def reviewer(data: Reviewer):
    request_data = data.dict()
    files = await store_data(request_data)
    locus = request_data.get('locus', '')
    print(locus, files)

    return f'''<svg
      version="1.1"
       baseProfile="full"
       width="800" height="100"
       xmlns="http://www.w3.org/2000/svg">

      <rect width="100%" height="100%" fill="red" />
      <text x="20" y="50" font-size="20" fill="black">
        1st url: {files[0]}
      </text>
    </svg>'''

