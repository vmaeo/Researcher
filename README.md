# Researcher

A local CLI research agent that autonomously searches and summarizes any topic using DuckDuckGo and Ollama's locally-run Llama 3.2 model.

---

## Example

```bash
python main.py "Artificial Intelligence breakthroughs 2026"
```

<p align="center">
<img width="600px" alt="researcher_example" src="https://github.com/user-attachments/assets/239290ef-5d2f-4672-855b-75e805c6c6c3" />
</p>

---

## Features

* Searches the web using DuckDuckGo
* Scrapes and parses webpages automatically
* Summarizes findings using a locally running Llama 3.2 model
* Saves every research session locally as a .json file
* Configurable search depth (number of pages scraped) through the --depth flag (defaults to 3)
* Dependencies: `typer`, `rich`, `ddgs`, `httpx`, `beautifulsoup4`

---

## Requirements

* Python 3.10+
* [Ollama](https://ollama.com)
* Llama 3.2 model pulled:
```bash
ollama pull llama3.2
```

---

## Installation

Clone depository
```bash
git clone https://github.com/vmaeo/Researcher.git
cd Researcher
```
Activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate  # Windows
```
Install dependencies
```bash
pip install rich typer ddgs httpx beautifulsoup4
```

---

## Usage

```bash
ollama serve
```
```bash
python main.py "your query"
```
Alternatively, with customized depth:
```bash
python main.py "your query" --depth 6
```

---

## Some Limitations

* The agent will skip websites that block automated scraping 
* The 3B model is known to occasionally hallucinate sources
* The speed is dependant on hardware

---

## Notes 

The nature / personality of this agent is easily modifiable through the ``connection.py`` file. Simply change the prompt variable within the summarize function.

## Future Improvements

* Creation of a `history` command that lists and reloads past sessions
* Better error handling for blocked URLs
* Support for other local models
