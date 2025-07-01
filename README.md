# Projeto: Análise de Preços de Produtos com Dados Públicos

Este projeto demonstra um pipeline completo de engenharia de dados utilizando Python, Airflow e Metabase, com dados reais extraídos da API pública da ANP (Agência Nacional do Petróleo) e do Banco Mundial.

## 🔧 Tecnologias Utilizadas

- **Python**: Scripts de extração, transformação e carga (ETL)
- **Airflow**: Orquestração dos scripts de ETL
- **SQLite**: Armazenamento local dos dados transformados
- **Metabase**: Visualização dos dados e geração de insights
- **Docker**: Containerização do ambiente

## 🧠 O que foi feito

1. **Extração de Dados**
   - Utilizamos a API da ANP e a API do Banco Mundial para coletar:
     - Preços médios de combustíveis no Brasil
     - PIB (Produto Interno Bruto) anual entre 2010 e 2020
   - Dados salvos inicialmente em formato `.csv` e `.parquet`.

2. **Transformação dos Dados**
   - Limpeza e tratamento dos dados utilizando pandas.
   - Normalização de formatos numéricos e remoção de inconsistências.
   - Conversão do PIB para milhões para facilitar a leitura nos dashboards.

3. **Carga em Banco de Dados**
   - Os dados tratados foram carregados em um banco SQLite.
   - Banco salvo no caminho: `data/processed/anp.db`.

4. **Orquestração com Airflow**
   - Dois scripts foram integrados em uma DAG no Airflow:
     - `extract_data` – responsável pela extração dos dados
     - `transform_data` – responsável pela limpeza e transformação
   - DAG validada com sucesso via interface Web do Airflow.

5. **Visualização com Metabase**
   - O Metabase foi conectado ao banco SQLite.
   - Gráficos e dashboards foram criados para analisar a evolução do PIB e outros indicadores ao longo dos anos.

## 🚀 Como Executar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/ThiagoAPC/pipeline-anp.git
   cd pipeline-anp
