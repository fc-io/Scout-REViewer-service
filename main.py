import uuid

from typing import Optional

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

from service.get_files import get_files
from service.generate_svg import generate_svg

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Scout-REViewer-service is running!"}

class Reviewer(BaseModel):
    reads: str
    reads_index: str
    vcf: str
    reference: Optional[str] = None
    reference_index: Optional[str] = None
    catalog: Optional[str] = None
    locus: str

@app.post('/reviewer', response_class=PlainTextResponse)
async def reviewer(request_data: Reviewer):
    file_id = str(uuid.uuid4())
    data = request_data.dict()
    files = await get_files(data, file_id)
    print('files')
    print(files)
    path_to_svg = generate_svg(data, file_id, files)

    return open(path_to_svg, "r").read()
