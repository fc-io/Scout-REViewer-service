import os
import asyncio
import async_timeout
import uuid
from aiohttp import ClientSession
import aiofiles as aiof

async def save(data, file_name_prefix, file_type):
    path = './tmp_data'
    file_id = str(uuid.uuid4())
    file_name = f'{path}/{file_name_prefix}_{file_id}.{file_type}'

    async with aiof.open(file_name, "wb") as out:
        await out.write(data)
        await out.flush()

    return {file_name_prefix: file_name}

async def get_data(session, data, data_type, file_type):
    url = data.get(data_type, '')
    respone = await session.get(url)
    file_name = await save(await respone.read(), data_type, file_type)

    return file_name

async def store_data(data):
    async with ClientSession() as session:
        tasks = []
        tasks.append(asyncio.create_task(get_data(session, data, 'catalog', 'json')))
        tasks.append(asyncio.create_task(get_data(session, data, 'reads', 'bam')))
        tasks.append(asyncio.create_task(get_data(session, data, 'vcf', 'vcf')))

        results = await asyncio.gather(*tasks)

        return results
