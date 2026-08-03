import requests
import json

BASE_URL = "https://www.mapper-rtc.com.br"

def consultar_api():
    
    versao = input("Digite a versao (ex: v1-01-00): ").strip()
    codigo_lc = input("Digite o item (ex: 01.01): ").strip()

    url = f"{BASE_URL}/{versao}/lc116/{codigo_lc}"
    
    print(f"\nFazendo requisicao para: {url} ...\n")

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            print("RESPOSTA DA API:")
            dados = response.json()
            print(json.dumps(dados, indent=2, ensure_ascii=False))
        else:
            print(f"Erro {response.status_code}: {response.text}")

    except Exception as e:
        print(f"Nao foi possivel conectar a API: {e}")

if __name__ == "__main__":
    consultar_api()