import pandas as pd

def construir_estrutura_hierarquica(df: pd.DataFrame) -> list:
    resultado = []

    # agrupa por item da lc116 
    for (item_lc, desc_item), grupo_item in df.groupby(["Item LC 116", "Descrição Item"], sort=False):
        
        item_dict = {
            "item_lc_116": str(item_lc).strip(),
            "descricao_item": str(desc_item).strip(),
            "servicos_nbs": []
        }

        # dentro do item agrupa por nbs (ignora linhas sem nbs)
        grupo_item_clean = grupo_item.dropna(subset=["NBS"])
        for (nbs_cod, nbs_desc), grupo_nbs in grupo_item_clean.groupby(["NBS", "DESCRIÇÃO NBS"], sort=False):
            
            nbs_dict = {
                "codigo": str(nbs_cod).strip(),
                "descricao": str(nbs_desc).strip(),
                "configuracoes_operacionais": []
            }

            # dentro da nbs agrupa pelas variacoes de parametros operacionais
            colunas_ops = ["PS ONEROSA? (S/N)", "ADQ EXTERIOR? (S/N)", "INDOP", "Local incidência IBS"]
            for (ps_on, adq_ext, indop, loc_ibs), grupo_op in grupo_nbs.groupby(colunas_ops, sort=False):
                
                op_dict = {
                    "ps_onerosa": str(ps_on).strip(),
                    "adq_exterior": str(adq_ext).strip(),
                    "IndOp": str(indop).strip(),
                    "local_incidencia_ibs": str(loc_ibs).strip(),
                    "classificacoes_tributarias": []
                }

                # classificacoes tributarias
                # percorre linha por linha para PERMITIR que itens duplicados aparecam no json 
                grupo_op_clean = grupo_op.dropna(subset=["cClassTrib"])
                for _, row in grupo_op_clean.iterrows():
                    op_dict["classificacoes_tributarias"].append({
                        "cClassTrib": str(row["cClassTrib"]).strip(),
                        "nome_cClassTrib": str(row["nome cClassTrib"]).strip()
                    })

                nbs_dict["configuracoes_operacionais"].append(op_dict)
                
            item_dict["servicos_nbs"].append(nbs_dict)
            
        resultado.append(item_dict)

    return resultado