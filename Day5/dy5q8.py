import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

def download(url):
    try:
        print(f"Downloading: {url}")
        response = requests.get(url, timeout=5)
        return response.text
    except:
        return ""

def get_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    return [urljoin(base_url, a['href']) for a in soup.find_all("a", href=True)]

def save(url, content):
    name = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
    with open(name, "w", encoding="utf-8") as f:
        f.write(content)

def main(url):
    html = download(url)
    save(url, html)
    links = get_links(html, url)

    with ThreadPoolExecutor() as executor:
        for content in executor.map(download, links):
            if content.strip():
                idx = executor._counter if hasattr(executor, '_counter') else 0
                save(f"link_{idx}", content)


