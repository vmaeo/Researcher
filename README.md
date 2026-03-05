# Researcher

A local CLI research agent that autonomously searches and summarizes any topic using DuckDuckGo and Ollama's locally-run Llama 3.2 model.

---

## Example

```
python main.py "Artificial Intelligence breakthroughs 2026"

                                                     ╭────────────╮
                                                     │ RESEARCHER │
                                                     ╰────────────╯
[Searching...]
[Reading: https://www.latest.com/belief-and-breakthrough-outlook-on-artificial-intelligence-development-trends]
[Reading: https://www.techallabout.com/artificial-intelligence-breakthroughs/]
[Reading: https://casinotips.io/category/gaming/artificial-intelligence/]
[Summarizing...]
Here is a structured summary of the provided notes, including important findings and sources:

Title: The Evolution of AI and its Impact on Society

Summary:

The AI industry is at a critical crossroads, with the technological competition between OpenAI and Google intensifying.
Despite challenges such as data depletion, the industry remains optimistic about the development of Artificial General
Intelligence (AGI). The Scaling Law, proposed by Huang Renxun, is the most reliable technical path for sustained growth
of computing power. Multimodal technology has ushered in a new era, enabling models to integrate text, images, and
videos, and breaking the limitation of large language models.

Key Findings:

 1 The AI industry is experiencing rapid growth and advancements, with the total installed capacity of large-scale data
   center projects exceeding 45 GW and $2.5 trillion in investment.
 2 Multimodal technology has enabled models to achieve in-depth integration of text, images, and videos, breaking the
   limitation of large language models.
 3 Innovations in underlying architectures and learning paradigms are flourishing, with emerging global laboratories
   taking diverse approaches to address challenges such as superintelligence safety, system reliability, and
   catastrophic forgetting.
 4 The AI4S field is transitioning from academic breakthroughs to industrial applications, with significant potential
   for impact in various industries.

Important Sources:
[...]
```

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
