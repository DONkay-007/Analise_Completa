
# 📊 Projeto de Análise de Vendas - Setor Agrícola



## 📖 Visão Geral do Projeto

Bem-vindo ao meu projeto de análise de dados focado em vendas no setor agrícola! Este repositório serve como uma demonstração prática das minhas habilidades em **coleta, limpeza, transformação, análise exploratória (EDA) e visualização de dados**. O objetivo é extrair insights valiosos a partir de um conjunto de dados de vendas de produtos agrícolas, simulando um cenário de negócios real.

Este é um projeto **em constante desenvolvimento**, e novas análises e visualizações serão adicionadas periodicamente. Sinta-se à vontade para acompanhar o progresso!

## 🎯 Objetivos

O principal objetivo deste projeto é aplicar técnicas de análise de dados para responder a perguntas de negócio cruciais, como:

*   ✅ **Limpeza e Pré-processamento:** Tratar dados ausentes, inconsistentes ("indefinido", "erro", "sem data") e garantir a qualidade para uma análise precisa.
*   📈 **Análise de Desempenho:** Identificar os produtos mais vendidos, as categorias mais lucrativas e os vendedores com melhor performance.
*   📅 **Análise Temporal:** Investigar tendências de vendas ao longo do tempo, identificando padrões de sazonalidade.
*   📦 **Gestão de Estoque:** Analisar a relação entre o volume em estoque e a quantidade de produtos vendidos.
*   📊 **Visualização de Dados:** Criar um dashboard interativo para apresentar os principais indicadores e descobertas de forma clara e intuitiva.

## 🗃️ O Conjunto de Dados

O dataset utilizado, `banco_agro_projeto.csv`, é um arquivo em formato CSV que contém registros de vendas de diversos produtos agrícolas.

#### Dicionário de Dados:

| Coluna | Descrição | Tipo de Dado (Original) | Observações |
| :--- | :--- | :--- | :--- |
| `Produto` | Nome do produto agrícola (ex: Café, Soja). | `Texto` | |
| `Categoria` | Categoria do produto (ex: Cereal, Grão, Fibra). | `Texto` | Apresenta inconsistências (ex: Arroz como Bebida). |
| `Estoque` | Quantidade do produto em estoque. | `Número` | Contém valores numéricos e a string "indefinido". |
| `Vendidos` | Quantidade de unidades vendidas. | `Número` | Possui valores nulos/vazios. |
| `Data_de_vendas` | Data da venda (formato AAAA-MM-DD). | `Data` | Contém a string "sem data". |
| `Data_venda` | Data da venda (formato DD/MM/AAAA). | `Data` | Redundante e contém a string "erro". |
| `Vendedor` | Nome do vendedor responsável pela transação. | `Texto` | Possui valores nulos/vazios. |

O tratamento das inconsistências e dos dados ausentes é um dos principais desafios e uma etapa fundamental deste projeto.

## 🛠️ Ferramentas e Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando o ecossistema Python para análise de dados, além de ferramentas de BI para a criação de dashboards.

*   **Linguagem de Programação:** `Python`
*   **Bibliotecas de Análise:** `Pandas`, `NumPy`
*   **Bibliotecas de Visualização:** `Matplotlib`, `Seaborn`, `Plotly`
*   **Ambiente de Desenvolvimento:** `Jupyter Notebook` / `VS Code`
*   **Ferramenta de BI (Dashboard):** `Power BI` / `Looker Studio` / `Tableau` (a ser definido)

## 📂 Estrutura do Repositório

O projeto está organizado da seguinte forma para facilitar a navegação:

```
├── 📄 README.md                <- Arquivo de apresentação que você está lendo.
├── 📁 data/
│   └── 📊 banco_agro_projeto.csv <- O conjunto de dados brutos.
├── 📁 notebooks/
│   └── 📈 eda_vendas_agricolas.ipynb <- Notebook com todo o processo de limpeza e análise.
└── 📁 dashboards/
    └── 🖼️ (em breve)             <- Arquivos ou links para os dashboards interativos.
```

## 🚀 Análise em Andamento e Próximos Passos

A análise será conduzida em etapas, começando pela limpeza e culminando na criação de visualizações interativas.

#### Etapas Planejadas:

1.  **Limpeza e Transformação dos Dados:**
    *   Unificar as colunas de data.
    *   Converter colunas para os tipos corretos (números e datas).
    *   Tratar valores ausentes nas colunas `Vendidos` e `Vendedor` (ex: substituindo por 0 ou "Não identificado").
    *   Padronizar a coluna `Estoque`, substituindo "indefinido" por um valor numérico (como a média ou 0).
    *   Corrigir as inconsistências na coluna `Categoria`.

2.  **Análise Exploratória (EDA):**
    *   **Ranking de Vendas:**
        *   Qual o produto mais vendido no geral?
        *   Qual a categoria de produto com maior volume de vendas?
        *   Quem são os 5 melhores vendedores?
    *   **Análise Temporal:**
        *   Qual o mês com o maior pico de vendas?
        *   As vendas de algum produto específico aumentam em alguma época do ano?
    *   **Análise de Estoque:**
        *   Existe uma correlação entre a quantidade em estoque e o volume de vendas?

3.  **Desenvolvimento do Dashboard:**
    *   Criar um painel visual com os principais KPIs (Indicadores-chave de Desempenho).
    *   Adicionar filtros interativos por produto, vendedor e período.

## 💡 Como Contribuir ou Entrar em Contato

Este é um projeto de portfólio pessoal, mas feedbacks e sugestões são sempre bem-vindos! Se você tiver alguma ideia ou dúvida, sinta-se à vontade para abrir uma *issue* neste repositório.

**Conecte-se comigo:**

*   **Email:** luisfilipemnovais@gmail.com

Obrigado pela sua visita