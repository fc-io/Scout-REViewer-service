import aiofiles as aiof
import async_timeout
import asyncio
import os
from aiohttp import ClientSession

async def save(data, file_name_prefix, file_id, file_type):
    path = './tmp_data'
    file_name = f'{path}/{file_id}_{file_name_prefix}.{file_type}'

    os.makedirs(path, exist_ok=True)

    async with aiof.open(file_name, "wb") as out:
        await out.write(data)
        await out.flush()

    return {file_name_prefix: file_name}

async def get_data(session, data, data_type, file_id, file_type):
    url = data.get(data_type, '')
    respone = await session.get(url)
    file_name = await save(await respone.read(), data_type, file_id, file_type)

    return file_name

async def store_data(file_id, data):
    async with ClientSession() as session:
        tasks = []
        tasks.append(asyncio.create_task(get_data(session, data, 'catalog', file_id, 'json')))
        tasks.append(asyncio.create_task(get_data(session, data, 'reads', file_id, 'bam')))
        tasks.append(asyncio.create_task(get_data(session, data, 'vcf', file_id, 'vcf')))

        results = await asyncio.gather(*tasks)

        return results
