import httpx

def summarize(notes: list) -> str:
    all_notes = " ".join(notes)
    
    prompt = f"""You are a research assistant. 
                Based on the following notes, provide a structured summary with important finding and sources: 
                {all_notes}"""
    
    response = httpx.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }, timeout=300)
    
    return response.json()["response"]