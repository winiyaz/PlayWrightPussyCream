# Your project using rich 
from rich.console import Console # For console.print
from rich.panel import Panel # For Panel()
def main():
    console = Console()
    panel = Panel("""
Enjoy StinlySmellySWeaty women
""",title="Mistress",subtitle="ToiletSlave", style="Italic", border_style="magenta")
    # Print the Panel
    console.print(panel)


if __name__ == "__main__":
    main()
