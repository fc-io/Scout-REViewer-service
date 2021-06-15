import aiofiles as aiof
import async_timeout
import asyncio
import os
from aiohttp import ClientSession
from service.utils.get_root_path import get_root_path
import urllib

async def save(data, file_name_suffix, file_id, file_type):
    path = f'{get_root_path()}/tmp_data'

    # The bam-index file need to have the same filename as the read-bam file
    # for REViewer to recognize it. So we have this check here and change the
    # suffix acordingly.
    suffix = 'reads' if file_name_suffix == 'index_file' else file_name_suffix
    file_name = f'{path}/{file_id}_{suffix}.{file_type}'
    os.makedirs(path, exist_ok=True)

    async with aiof.open(file_name, "wb") as out:
        await out.write(data)
        await out.flush()

    return {file_name_suffix: file_name}

async def get_data(session, data, data_type, file_id, file_type):
    url = data.get(data_type, '')

    # if path (non url) we don't need to fetch and store the file and can just
    # use the file directly
    if (urllib.parse.urlparse(url).scheme == ''):
        return {data_type: url}

    respone = await session.get(url)
    file_name = await save(await respone.read(), data_type, file_id, file_type)

    return file_name

async def store_data(data, file_id):
    async with ClientSession() as session:
        results = await asyncio.gather(
            asyncio.create_task(get_data(session, data, 'catalog', file_id, 'json')),

            asyncio.create_task(get_data(session, data, 'reads', file_id, 'bam')),
            asyncio.create_task(get_data(session, data, 'index_file', file_id, 'bam.bai')),

            asyncio.create_task(get_data(session, data, 'vcf', file_id, 'vcf'))
        )

        return {**results[0], **results[1], **results[2], **results[3]}
