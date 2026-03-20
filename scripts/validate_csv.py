from pathlib import Path
import csv

for path in Path('docs').rglob('*.csv'):
    with path.open(encoding='utf-8') as f:
        list(csv.reader(f))
    print(f'OK: {path}')
