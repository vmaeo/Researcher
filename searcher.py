from ddgs import DDGS
import httpx
from bs4 import BeautifulSoup

def search(query, num_results=5):
    searcher = DDGS()
    results = searcher.text(query, max_results=num_results)
    return results

def scrape(url):
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    text = " ".join([p.get_text() for p in paragraphs])
    return text[:2000]