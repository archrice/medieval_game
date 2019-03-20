import re
import os
import json


cwd = os.getcwd()


with open(f"{cwd}/woods.py", 'r') as w:
    wds = w.read()


with open(f"{cwd}/castle.py", 'r') as w:
    castle = w.read()

with open(f"{cwd}/town.py", 'r') as w:
    town = w.read()


with open(f"{cwd}/cave.py", 'r') as w:
    cave = w.read()


txt = (wds+castle+town+cave)


pattern = re.compile(r'".*"')
pattern2 = re.compile(r"'.*'")

matches = pattern.finditer(txt)
matches2 = pattern2.finditer(txt)

for m in matches:
    print(m)
    with open(f"{cwd}/script.txt", 'w', encoding='utf-8') as f:
        f.write(str(m))

for m in matches2:
    print(m)
    with open(f"{cwd}/script.txt", 'w', encoding='utf-8') as f:
        f.write(str(m))

