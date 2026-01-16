import json
from rich.console import Console
from rich.panel import Panel
from fuzzywuzzy import fuzz

console = Console()

with open("dataset.json", "r") as file:
    dataset = json.load(file)

console.print(Panel("🤖 SMART AI AGENT\nAsk me anything!", style="bold cyan"))

while True:
    user_input = console.input("[bold green]You ➜ [/bold green]").lower()

    if user_input == "exit":
        console.print("[bold red]AI ➜ Goodbye 👋[/bold red]")
        break

    best_match = None
    highest_score = 0

    for data in dataset:
        score = fuzz.ratio(user_input, data["question"])
        if score > highest_score:
            highest_score = score
            best_match = data["answer"]

    if highest_score > 60:
        console.print(Panel(f"🤖 {best_match}", style="bold magenta"))
    else:
        console.print(Panel("🤖 I am still learning… 🧠", style="yellow"))
