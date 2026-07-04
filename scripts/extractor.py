import pandas as pd
from pathlib import Path

def ler_e_preparar_excel(excel_path: Path) -> pd.DataFrame:
    # carrega todas as colunas como string 
    df = pd.read_excel(excel_path, sheet_name="tabela geral", dtype=str)
    
    # remove espacos em branco nos nomes das colunas
    df.columns = df.columns.str.strip()
    
    # colunas que sofrem com o efeito de celulas mescladas na planilha
    colunas_ffill = [
        "Item LC 116", "Descrição Item", "NBS", "DESCRIÇÃO NBS",
        "PS ONEROSA? (S/N)", "ADQ EXTERIOR? (S/N)", "INDOP", "Local incidência IBS",
        "cClassTrib", "nome cClassTrib"
    ]
    
    df[colunas_ffill] = df[colunas_ffill].ffill()
    
    return df