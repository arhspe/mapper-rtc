import os
import json
from typing import Optional, Dict

JSON_PATH = os.path.join("data", "processed", "v1_01_00", "correlacao.json")

_indice_lc116: Dict[str, dict] = {}
_indice_nbs: Dict[str, dict] = {}

def initialize_search_service():
    
    global _indice_lc116, _indice_nbs
    
    if not os.path.exists(JSON_PATH):
        print(f"arquivo de dados não encontrado em {JSON_PATH}")
        return

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        lista_correlacao = json.load(f)

    for item in lista_correlacao:
      
        codigo_lc = item.get("item_lc_116")
        if codigo_lc:
            _indice_lc116[codigo_lc] = item

        
        for nbs_item in item.get("servicos_nbs", []):
            codigo_nbs = nbs_item.get("nbs")
            if codigo_nbs:
                _indice_nbs[codigo_nbs] = item

    print(f"{len(_indice_lc116)} itens fiscais carregados com sucesso.")

def get_by_lc116(codigo: str) -> Optional[dict]:

    return _indice_lc116.get(codigo.strip())

def get_by_nbs(codigo: str) -> Optional[dict]:
   
    return _indice_nbs.get(codigo.strip())