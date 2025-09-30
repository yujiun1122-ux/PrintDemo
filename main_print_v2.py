from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

# 데이터 정의
name = "Alice"
age = 25
score = 95.5

data = {"name": name, "age": age, "score": score}

# 단순 출력 / 스타일 적용
rprint(f"[bold green]Hello, {name}![/] Your score is [cyan]{score:.2f}[/].")

# Panel + 텍스트 출력
panel_text = (
    "[bold]Student Info[/]\n"
    f" - Name: [yellow]{name}[/]\n"
    f" - Age: [yellow]{age}[/]\n"
    f" - Score: [cyan]{score:.2f}[/]"
)
rprint(Panel(panel_text, title="Profile", border_style="blue"))

# Table 출력 (딕셔너리 리스트를 표로 정리)
table = Table(title="Records", title_style="bold")
table.add_column("Key", style="cyan")
table.add_column("Value", style="magenta")

for k, v in data.items():
    table.add_row(str(k), str(v))

rprint(table)

# sep, end 옵션 사용 (rich.print도 동일 동작)
rprint(2023, "09", "27", sep="-", end="\n\n")

