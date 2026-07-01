<div align="center">

<img src="logo.png" alt="Mapper RTC Logo" width="150">

  # Mapper RTC

  ![Status](https://img.shields.io/badge/Status-Online-brightgreen)
  ![v2.0.0](https://img.shields.io/badge/v2.0.0-f97316?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iMi41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLXRhZy1pY29uIGx1Y2lkZS10YWciPjxwYXRoIGQ9Ik0xMi41ODYgMi41ODZBMiAyIDAgMCAwIDExLjE3MiAySDRhMiAyIDAgMCAwLTIgMnY3LjE3MmEyIDIgMCAwIDAgLjU4NiAxLjQxNGw4LjcwNCA4LjcwNGEyLjQyNiAyLjQyNiAwIDAgMCAzLjQyIDBsNi41OC02LjU4YTIuNDI2IDIuNDI2IDAgMCAwIDAtMy40MnoiLz48Y2lyY2xlIGN4PSI3LjUiIGN5PSI3LjUiIHI9Ii41IiBmaWxsPSJjdXJyZW50Q29sb3IiLz48L3N2Zz4=)
  [![License](https://img.shields.io/badge/license-Apache%202.0-orange)](https://opensource.org/licenses/Apache-2.0)

  [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
  [![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org)
  [![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat&logo=pydantic&logoColor=white)](https://docs.pydantic.dev)
  
</div>

`mapper-rtc` é uma API desenvolvida em Python com FastAPI para simplificar a consulta de correlações fiscais trazidas pela Reforma Tributária do Consumo. Focada na estrutura do _[Anexo VIII](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/anexoviii-correlacaoitemnbsindopcclasstrib_ibscbs_v1-01-00.xlsx)_, ela mapeia a relação entre os itens da _[Lei Complementar nº 116, de 31 de julho de 2003](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp116.htm)_ e os novos indexadores do **IBS** e **CBS**, cruzando códigos **NBS**, parâmetros de operação (`cIndOp`) e classificações tributárias (`cClassTrib`).

A API adota uma arquitetura de dados em memória. Os arquivos JSON são lidos e indexados em dicionários apenas uma vez, no momento em que a aplicação inicializa.

> [!WARNING]
> **Projeto Independente e Sem Vínculo Governamental**. Esta API não possui qualquer ligação com a Receita Federal. O software é distribuído gratuitamente sob a _Licença Apache 2.0_


### Documentação da API (Swagger) 📑

A API conta com uma interface interativa e auto-documentada utilizando o padrão OpenAPI (Swagger). Nela, você pode visualizar todos os schemas de dados, contratos e testar as requisições em tempo real diretamente pelo navegador. _[Acesse aqui a Documentação Oficial](http://mapper-rtc.com.br/docs)_

### Endpoints Disponíveis 🗺️

Os endpoints listados abaixo contemplam mapeamentos estruturados de acordo com as diretrizes e parâmetros oficiais da Reforma.

> [!IMPORTANT]
> **Nota sobre Atualizações:** A API foi arquitetada para receber atualizações manuais e incrementais à medida que novas versões da tabela de correlação forem disponibilizadas oficialmente no portal do _[Ambiente Nacional da NFS-e (RTC)](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc)_.

Abaixo estão descritas as operações disponíveis, utilizando como exemplo as rotas da versão `v1_00_00`:

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/status` | Healthcheck (Verifica se a API está online). |
| `GET` | `/v1_00_00/lc116/{code}` | Retorna as correlações da LC 116/03 para IBS/CBS. |
