import asyncio
import async_timeout
from aiohttp import ClientSession

async def fetch_url(session, url):
    """Fetch the specified URL using the aiohttp session specified."""
    response = await session.get(url)
    return {'url': response.url, 'status': response.status}

async def get_all_urls(urls):
    """Retrieve the list of URLs asynchronously using aiohttp."""
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_url(session, url))
            tasks.append(task)

        results = await asyncio.gather(*tasks)

        return results
