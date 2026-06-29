import os
import json


_DATA_STORE = {}

def initialize_search_service():
    global _DATA_STORE
    _DATA_STORE = {}
    
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/processed"))
    
    if not os.path.exists(base_dir):
        print(f"[warning] diretorio de dados nao encontrado em: {base_dir}")
        return

    versions = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d.startswith('v')]
    
    for version in versions:
        version_path = os.path.join(base_dir, version)
        corr_file = os.path.join(version_path, "correlacao.json")
        
        if os.path.exists(corr_file):
            with open(corr_file, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    
                    _DATA_STORE[version] = {
                        "lc116": {},
                        "nbs": {}
                    }
                    
                    for item in data:
                        lc_code = item.get("item_lc_116")
                        if lc_code:
                            _DATA_STORE[version]["lc116"][lc_code] = item
                        
                        for nbs_item in item.get("servicos_nbs", []):
                            nbs_code = nbs_item.get("nbs")
                            if nbs_code:
                                _DATA_STORE[version]["nbs"][nbs_code] = item
                                
                    print(f"[info] versao {version} carregada com sucesso")
                except Exception as e:
                    print(f"[error] erro ao carregar .json da versao {version}: {e}")

def get_by_lc116(version: str, code: str):
    return _DATA_STORE.get(version, {}).get("lc116", {}).get(code)

def get_by_nbs(version: str, code: str):
    return _DATA_STORE.get(version, {}).get("nbs", {}).get(code)