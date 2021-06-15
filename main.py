import uuid

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import Optional

from service.request_data import store_data
from service.generate_svg import generate_svg

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Is working!"}

class Reviewer(BaseModel):
    reads: str
    index_file: str
    vcf: str
    catalog: Optional[str] = None
    locus: str

@app.post('/reviewer', response_class=PlainTextResponse)
async def reviewer(data: Reviewer):
    file_id = str(uuid.uuid4())
    request_data = data.dict()
    results = await store_data(request_data, file_id)
    svg_path = generate_svg(request_data, file_id, results)

    return open(svg_path, "r").read()
    return ''

