import asyncio
import requests
from bs4 import BeautifulSoup
import aiohttp
from urllib.parse import urljoin

def extract_links(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    return [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

async def fetch(session, url):
    try:
        async with session.get(url) as resp:
            print(f"Fetched {url} ({resp.status})")
            return await resp.text()
    except Exception as e:
        print(f"Failed {url}: {e}")
        return None

async def download_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, u) for u in urls]
        return await asyncio.gather(*tasks)
        
def main(url):
    links = extract_links(url)
    print(f"Found {len(links)} links.")
    asyncio.run(download_all(links))

if __name__ == "__main__":
    main("https://request.com")
