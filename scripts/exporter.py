import json
from pathlib import Path

def salvar_json(dados: list, destino_path: Path):
    destino_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(destino_path, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)