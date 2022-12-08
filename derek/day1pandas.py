import pandas as pd
import pathlib

body = pathlib.Path("sample/calorie_input.txt").read_text()
df = pd.DataFrame({"calories": pd.to_numeric(body.splitlines())})
df["elf"] = df.isnull().cumsum()
elf_totals = df.groupby("elf").calories.sum().sort_values()
print("answer 1:", elf_totals.tail(1).sum())
print("answer 2:", elf_totals.tail(3).sum())
