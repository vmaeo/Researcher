from storage import create_session, save_session
from searcher import search, scrape
from connection import summarize
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def run(query, depth):
    session = create_session(query)
    print("[Searching...]")
    results = search(query, depth)

    for result in results:
        url = result["href"]
        print(f"[Reading: {url}]")
        scraped_url = scrape(url)
        session["notes"].append(scraped_url)
        session["sources"].append(url)
    
    print("[Summarizing...]")
    session["summary"] = summarize(session["notes"])
    save_session(session)
    console.print(Markdown(session["summary"]))