#!/usr/bin/env python3
import typer
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from agent import run

console = Console()

def print_banner():
    console.print(Align(Panel(
        "[bold white]RESEARCHER[/bold white]",
        style="bold white",
        expand=False
    ), align="center"))

app = typer.Typer()

@app.command()
def research(query: str, depth: int = 3):
      print_banner()
      run(query, depth)

if __name__ == "__main__":
    app()