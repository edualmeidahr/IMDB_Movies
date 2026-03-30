import os

folders = [
    'data/raw',
    'data/processed',
    'notebooks',
    'reports/figures',
    'src',
    'models'
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Pasta criada: {folder}")