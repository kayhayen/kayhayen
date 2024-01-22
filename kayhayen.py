from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🤓 [link=https://kay.nuitka.net]Kay Hayen", guide_style="bold cyan")
python_tree = tree.add("🐍 Python expert", guide_style="green")
python_tree.add("⭐ [link=https://github.com/Nuitka/Nuitka]Nuitka")
python_tree.add("⭐ [link=https://github.com/Nuitka/Nuitka-Python]CPython fork for Nuitka")
python_tree.add("⭐ [link=https://github.com/Nuitka/Nuitka-Action]Github Action for Nuitka")
full_stack_tree = tree.add("🔧 Full-stack developer")
family_tree = tree.add("👪 Family", guide_style="yellow")
family_tree.add("My wife Anna (Nuitka)")
family_tree.add("My 3 kids")

about = """\
I'm a commercial and Free Software developer, living in \
[link=https://maps.app.goo.gl/DSo3SNtRpz3Eb3pd9]Karlsruhe[/], Germany.

Other than software development, my passion would be no other. It's my \
life mission to create the best Python Compiler I can possibly do or \
die trying, ... of old age.

[green]Follow me on Twitter [bold link=https://twitter.com/kayhayen]@kayhayen[/]
[purple]Follow me on Mastodon [bold link=https://fosstodon.org/@kayhayen]@kayhayen[/]
"""


panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi there", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
