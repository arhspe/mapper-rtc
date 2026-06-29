from pathlib import Path
import json
import pandas as pd

RAW_DIR = Path("../data/raw")
PROCESSED_DIR = Path("../data/processed")

def automatizar_processamento():

    if not RAW_DIR.exists():
        print("pasta data/raw nao encontrada.")
        return

    raw_versions = {
        pasta.name
        for pasta in RAW_DIR.iterdir()
        if pasta.is_dir()
    }

    processed_versions = set()

    if PROCESSED_DIR.exists():
        processed_versions = {
            pasta.name
            for pasta in PROCESSED_DIR.iterdir()
            if pasta.is_dir()
        }

    novas_versoes = sorted(raw_versions - processed_versions)

    print(f"versoes encontradas: {len(raw_versions)}")
    print(f"ja processadas: {len(processed_versions)}")
    print(f"novas: {len(novas_versoes)}")
    print()

    if not novas_versoes:
        print("nenhuma versao nova encontrada")
        return

    for versao in novas_versoes:

        print(f"processando {versao}")

        pasta_raw = RAW_DIR / versao
        pasta_processed = PROCESSED_DIR / versao

        excel_files = list(pasta_raw.glob("*.xlsx"))

        if len(excel_files) == 0:
            print(f"erro: nenhuma planilha encontrada")
            continue

        if len(excel_files) > 1:
            print(f"erro: mais de uma planilha encontrada")
            continue

        excel_path = excel_files[0]

        df = pd.read_excel(
            excel_path,
            sheet_name="tabela geral",
            dtype=str
        )

        df.columns = df.columns.str.strip()

        colunas_pai = [
            "Item LC 116",
            "Descrição Item",
            "PS ONEROSA? (S/N)",
            "ADQ EXTERIOR? (S/N)",
            "INDOP",
            "Local incidência IBS"
        ]

        df[colunas_pai] = df[colunas_pai].ffill()

        resultado = []

        for valores_pai, grupo in df.groupby(colunas_pai):

            (
                item_lc,
                desc_item,
                ps_onerosa,
                adq_exterior,
                indop,
                local_ibs
            ) = valores_pai

            nbs_list = [
                {
                    "nbs": str(n).strip(),
                    "descricao_nbs": str(d).strip()
                }
                for n, d in grupo[
                    ["NBS", "DESCRIÇÃO NBS"]
                ].dropna(subset=["NBS"]).drop_duplicates().values
            ]

            class_list = [
                {
                    "cClassTrib": str(c).strip(),
                    "nome_cClassTrib": str(n).strip()
                }
                for c, n in grupo[
                    ["cClassTrib", "nome cClassTrib"]
                ].dropna(subset=["cClassTrib"]).drop_duplicates().values
            ]

            resultado.append({

                "item_lc_116": str(item_lc).strip(),

                "descricao_item": str(desc_item).strip(),

                "parametros_operacao": {

                    "ps_onerosa": str(ps_onerosa).strip(),

                    "adq_exterior": str(adq_exterior).strip(),

                    "cIndOp": str(indop).strip(),

                    "local_incidencia_ibs": str(local_ibs).strip()

                },

                "servicos_nbs": nbs_list,

                "classificacoes_tributarias": class_list

            })

        pasta_processed.mkdir(parents=True, exist_ok=True)

        with open(
            pasta_processed / "correlacao.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                resultado,
                f,
                indent=2,
                ensure_ascii=False
            )


        print(f"correlacao.json criado")
        print()

    print("pipeline finalizada com sucesso")


if __name__ == "__main__":
    automatizar_processamento()