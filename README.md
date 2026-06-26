<div align="center">

  # Mapper RTC

  [![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
  [![API Status](https://img.shields.io/badge/API_Status-Online-brightgreen?logo=statuspage&logoColor=white)](http://mapper-rtc.com.br/docs)
  [![Architecture](https://img.shields.io/badge/Arquitetura-In--Memory-blueviolet?logo=speedtest&logoColor=white)](#)
  [![License](https://img.shields.io/badge/license-Apache%202.0-orange)](https://opensource.org/licenses/Apache-2.0)

</div>

`mapper-rtc` é uma API desenvolvida em Python com FastAPI para simplificar a consulta de correlações fiscais trazidas pela Reforma Tributária do Consumo. Ela mapeia a relação entre os itens da _[Lei Complementar nº 116, de 31 de julho de 2003](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp116.htm)_ e os novos indexadores do **IBS** e **CBS**, cruzando códigos **NBS**, parâmetros de operação (`cIndOp`) e classificações tributárias (`cClassTrib`).

A API adota uma arquitetura de dados em memória. Os arquivos JSON são lidos e indexados em dicionários apenas uma vez, no momento em que a aplicação inicializa.

> [!WARNING]
> **Projeto Independente e Sem Vínculo Governamental**. Esta API não possui qualquer ligação com a Receita Federal. O software é distribuído gratuitamente sob a _Licença Apache 2.0_


### Documentação da API (Swagger) 📑

A API conta com uma interface interativa e auto-documentada utilizando o padrão OpenAPI (Swagger). Nela, você pode visualizar todos os schemas de dados, contratos e testar as requisições em tempo real diretamente pelo navegador. _[Acesse aqui a Documentação Oficial](http://mapper-rtc.com.br/docs)_

### Endpoints Disponíveis 🗺️

Os endpoints listados abaixo contemplam mapeamentos estruturados de acordo com as diretrizes e parâmetros oficiais da Reforma.

> [!IMPORTANT]
> **Nota sobre Atualizações:** A API foi arquitetada para receber atualizações manuais e incrementais à medida que novas versões da tabela de correlação forem disponibilizadas oficialmente no portal do _[Ambiente Nacional da NFS-e (RTC)](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc)_.

Abaixo estão descritas as operações disponíveis, utilizando como exemplo as rotas da versão `v1_01_00`:

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/status` | Healthcheck (Verifica se a API está online). |
| `GET` | `/v1_01_00/lc116/{code}` | Retorna as correlações da LC 116/03 para IBS/CBS. |
| `GET` | `/v1_01_00/nbs/{code}` | Retorna as correlações a partir do código NBS. |