import os
import json
import glob
import pandas as pd

def automatizar_processamento():
    pasta_raw = 'data/raw'
    
    pastas_versoes = [os.path.basename(p) for p in glob.glob(os.path.join(pasta_raw, 'v*')) if os.path.isdir(p)]
    
    if not pastas_versoes:
        print("nenhuma pasta de versao encontrada em data/raw/")
        return

    for versao in pastas_versoes:
        caminho_raw_versao = os.path.join(pasta_raw, versao)
        caminho_processed_versao = f'data/processed/{versao}'
        json_path = os.path.join(caminho_processed_versao, 'correlacao.json')
        
        arquivos_excel = glob.glob(os.path.join(caminho_raw_versao, '*.xlsx'))
        
        if not arquivos_excel:
            print(f"{versao} encontrada, mas sem arquivo para processar")
            continue
            
        excel_path = arquivos_excel[0] 

        if os.path.exists(json_path):
            print(f"{versao} já possui .json processado")
            continue

        print(f"versao nova detectada, processando {versao}...")

        df = pd.read_excel(excel_path, sheet_name='tabela geral', dtype=str)
        df.columns = df.columns.str.strip()

        colunas_pai = ['Item LC 116', 'Descrição Item', 'PS ONEROSA? (S/N)', 'ADQ EXTERIOR? (S/N)', 'INDOP', 'Local incidência IBS']
        df[colunas_pai] = df[colunas_pai].ffill()

        resultado = []
        for valores_pai, grupo in df.groupby(colunas_pai):
            item_lc, desc_item, ps_onerosa, adq_exterior, indop, local_ibs = valores_pai
            
            nbs_list = [{"nbs": str(n).strip(), "descricao_nbs": str(d).strip()} 
                        for n, d in grupo[['NBS', 'DESCRIÇÃO NBS']].dropna(subset=['NBS']).drop_duplicates().values]
            
            class_list = [{"cClassTrib": str(c).strip(), "nome_cClassTrib": str(n).strip()} 
                          for c, n in grupo[['cClassTrib', 'nome cClassTrib']].dropna(subset=['cClassTrib']).drop_duplicates().values]
                    
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

        os.makedirs(caminho_processed_versao, exist_ok=True)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(resultado, f, indent=2, ensure_ascii=False)
            
        print(f"{versao} gerada com sucesso em {json_path}")

if __name__ == '__main__':
    automatizar_processamento()