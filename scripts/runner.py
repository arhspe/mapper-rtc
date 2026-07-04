from pathlib import Path
from extractor import ler_e_preparar_excel
from transform import construir_estrutura_hierarquica
from exporter import salvar_json

RAW_DIR = Path("../data/raw")
PROCESSED_DIR = Path("../data/processed")

def rodar_pipeline():
    if not RAW_DIR.exists():
        print("pasta data/raw nao encontrada")
        return

    # descobre novas versoes comparando as pastas raw e processed
    novas_versoes = sorted(
        {p.name for p in RAW_DIR.iterdir() if p.is_dir()} -
        {p.name for p in PROCESSED_DIR.iterdir() if PROCESSED_DIR.exists() and p.is_dir()}
    )

    if not novas_versoes:
        print("nenhuma versao nova encontrada")
        return

    for versao in novas_versoes:
        print(f"processando {versao}")
        
        pasta_raw = RAW_DIR / versao
        excel_files = list(pasta_raw.glob("*.xlsx"))

        if len(excel_files) == 0:
            print(f"erro: nenhuma planilha encontrada")
            continue

        if len(excel_files) > 1:
            print(f"erro: mais de uma planilha encontrada")
            continue

        df_limpo = ler_e_preparar_excel(excel_files[0])
        dados_estruturados = construir_estrutura_hierarquica(df_limpo)
        
        caminho_saida = PROCESSED_DIR / versao / "correlacao.json"
        salvar_json(dados_estruturados, caminho_saida)
        
        print(f"{caminho_saida.name} gerado para {versao}\n")

if __name__ == "__main__":
    rodar_pipeline()