```text
___  ___                             ______ _____ _____    |
|  \/  |                             | ___ \_   _/  __ \   |  Serviço de consulta e mapeamento 
| .  . | __ _ _ __  _ __   ___ _ __  | |_/ / | | | /  \/   |  entre a Lei Complementar nº 116
| |\/| |/ _` | '_ \| '_ \ / _ \ '__| |    /  | | | |       |  e os novos códigos de IBS/CBS.
| |  | | (_| | |_) | |_) |  __/ |    | |\ \  | | | \__/\   |
\_|  |_/\__,_| .__/| .__/ \___|_|    \_| \_| \_/  \____/   |  release: v1.0.0   License: Apache 2.0
             | |   | |                                     |  Python: 3.12+     Status: Active
             |_|   |_|                                          
```
**Mapper RTC** é uma API desenvolvida em `Python` com `FastAPI` para simplificar a consulta de correlações fiscais trazidas pela Reforma Tributária do Consumo. 

O projeto utiliza como base o `Anexo VIII` e relaciona os itens da [Lei Complementar nº 116 de 2003](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp116.htm) aos novos códigos do IBS e da CBS, cruzando códigos NBS, indicadores de operação (`cIndOp`) e classificações tributárias (`cClassTrib`).

A API adota uma **arquitetura de dados em memória**. As informações são lidas e indexadas uma única vez durante a inicialização da aplicação.

### 📁 Estrutura do projeto

```text
mapper-rtc/
│
├── app/                         # codigo-fonte da api
│   ├── models/                  # modelos e schemas 
│   ├── routes/                  # definicao dos endpoints
│   ├── services/                # regras de negocio
│   └── main.py                  # ponto de entrada da aplicacao
│
├── data/
│   ├── raw/                     # planilhas oficiais (.xlsx)
│   └── processed/               # arquivos JSON processados
│
├── scripts/                     # pipeline de processamento dos dados
│   ├── extractor.py             # extracao dos dados das planilhas
│   ├── transform.py             # transformacao e normalizacao dos dados
│   ├── exporter.py              # exportacao para JSON
│   └── runner.py                # executa todo o pipeline 
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

### ⚙️ Como os dados são processados 

Os dados têm origem nas planilhas oficiais de correlação publicadas pelo [Ambiente Nacional da NFS-e](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc), disponibilizadas no formato `.xlsx`.

O processamento dos dados pode ser dividido em duas etapas: **preparação** e **execução**.

Durante a preparação, as planilhas são armazenadas na pasta `/data/raw`. Em seguida, os scripts em `/scripts` realizam a extração, normalização e transformação dessas informações, gerando arquivos **JSON** estruturados na pasta `/data/processed`.

Na etapa de execução, a API carrega todos os arquivos JSON presentes em `/data/processed` durante sua inicialização. Esses dados são indexados em memória e permanecem disponíveis durante todo o ciclo de vida da aplicação.

> [!IMPORTANT]
> O projeto foi arquitetado para receber atualizações manuais, acompanhando o lançamento de novas planilhas publicadas pelo **Ambiente Nacional**.

O fluxo pode ser representado da seguinte forma:

```text
[ Preparação dos Dados ]
.xlsx ──> /data/raw ──> /scripts ──> /data/processed (.json)
                                            │
                                     (Carga Inicial)
                                            ▼
[ Execução da API ]
Endpoints <── Indexação em Memória <── Inicialização
```

Se precisar atualizar ou reprocessar as planilhas da pasta `/data/raw`:
```bash
python scripts/runner.py
```

### 📑 Documentação da API 

A API segue o padrão **OpenAPI** e disponibiliza uma interface do **Swagger UI**, onde é possível visualizar os endpoints e testar as requisições diretamente pelo navegador.

### 🗺️ Endpoints Disponíveis 

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/status` | Verifica a disponibilidade da API e fornece informações de execução. |
| `GET` | `/{version}/lc116/{code}` | Consulta as correlações de um item da LC 116/2003 para uma versão específica do Anexo VIII. |

O parâmetro `{version}` identifica a versão da tabela de correlação utilizada na consulta. Atualmente, a API disponibiliza as seguintes versões:

| Versão | Descrição |
| :--- | :--- |
| `v1-00-00` | Primeira versão publicada do Anexo VIII. |
| `v1-01-00` | Primeira atualização oficial do Anexo VIII. |

### 🚀 Executando localmente

**Pré-requisitos**

``` text
Python 3.12+
Git
```
**Clone o repositório**

```bash
git clone https://github.com/arhspe/mapper-rtc.git
```

```bash
cd mapper-rtc
```
**Crie um ambiente virtual**

_Linux/macOS_

```bash
python -m venv .venv
```
```bash
source .venv/bin/activate
```

_Windows_

```powershell
python -m venv .venv
```
```powershell
.venv\Scripts\activate
```

**Instale as dependências**

```bash
pip install -r requirements.txt
```

**Execute a aplicação**

```bash
uvicorn app.main:app --reload
```

Após a inicialização, a API estará disponível em:

```
http://localhost:8000
```
> _A rota raiz redireciona automaticamente para a documentação interativa do Swagger._

### 📋 Aviso

> Mapper RTC é um projeto independente, de caráter informativo e sem vínculo com órgãos públicos. As informações disponibilizadas podem conter inconsistências ou não refletir imediatamente alterações na legislação vigente. O autor e os colaboradores não se responsabilizam por eventuais prejuízos decorrentes do uso deste projeto. Caso identifique alguma inconsistência ou tenha sugestões de melhoria, entre em contato pelo e-mail arhspe.dev@gmail.com.

### 📄 Licença

O projeto é distribuído sob a licença **Apache 2.0**. Para mais detalhes, consulte [LICENSE](LICENSE).
