# This will be imported into main 

from rich.panel import Panel # For Panel()
from rich.console import Console # For console.print
console = Console() # Standard code to access console

def mistress():
    text1 = "Enjoy StinlySmellySWeaty women"
    panel = Panel.fit(text1 ,title="Mistress",subtitle="ToiletSlave", style="Italic", border_style="magenta")
    #    Print the Panel
    console.print(panel)
    
