# 📊 Projeto de Análise de Vendas - Setor Agrícola

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![PowerBI](https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi&logoColor=black) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=matplotlib&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-76B900?logo=seaborn&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white) ![YData-Profiling](https://img.shields.io/badge/YData_Profiling-00BFFF?logo=python&logoColor=white)

---

## 📖 Visão Geral do Projeto

Bem-vindo ao meu projeto de análise de dados focado em vendas no setor agrícola! Este repositório demonstra habilidades em **coleta, limpeza, transformação, análise exploratória (EDA) e visualização de dados**. O objetivo é extrair insights valiosos de um conjunto de dados de vendas agrícolas, simulando um cenário real de negócio.

---

## 🎯 Objetivos

- ✅ **Limpeza e Pré-processamento:** Tratamento de dados inconsistentes para garantir a qualidade da análise.
- 📈 **Análise de Desempenho:** Avaliação de performance por produtos e vendedores.
- 📅 **Análise Sazonal:** Identificação de padrões de vendas ao longo do tempo.
- 📦 **Correlação de Estoque:** Análise da relação entre níveis de estoque e volume de vendas.
- 📊 **Visualização de Dados:** Criação de dashboards interativos e relatórios automatizados para suportar a tomada de decisão.

---

## 🗃️ Conjunto de Dados

O projeto utiliza o arquivo `banco_agro_projeto.csv`, que contém informações sobre produtos agrícolas, estoque, vendas, vendedores e datas.

*Observação: O dataset poderia ser em formato `.xlsx` ou até mesmo um banco de dados (`.db`). A abordagem inicial de extração mudaria, mas os processos de tratamento e análise permaneceriam os mesmos.*

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas de Análise:** Pandas, NumPy
- **Bibliotecas de Visualização:** Matplotlib, Seaborn, Plotly
- **Análise Exploratória Automatizada:** YData-Profiling
- **Interface Web Interativa:** Streamlit
- **Machine Learning:** Scikit-Learn
- **BI e Dashboard:** Power BI / Looker Studio / Tableau

---

## 🗂 Estrutura do Projeto

```
📁 Projeto/
│
├── 📄 app.py                     # Aplicação principal em Streamlit
├── 📄 calculations.ipynb         # Notebook com extração e cálculos analíticos
├── 📄 clear.ipynb                # Notebook responsável pela limpeza e tratamento dos dados
├── 📄 Guia.md                    # Guia detalhado com todos os passos do projeto (ETL e análise)
├── 📄 README.md                  # Documento principal explicando o projeto
├── 📄 requirements.txt           # Lista de dependências do projeto
├── 📄 workflow_n8n.json          # Workflow de integração com o n8n
│
├── 📁 data/                      
│   └── banco_agro_projeto.csv
│   └── banco_agro_projeto_limpo.csv
│
├── 📁 venv/                      
│
├── 📁 __pycache__/               
│
├── 📁 .ipynb_checkpoints/        
│
└── 📁 .vscode/                  
```

---

## 🧭 Estrutura do App Streamlit

1.  **📂 Dataset** — Permite a visualização e aplicação de filtros nos dados, com opção de download em formato `.xlsx`.
2.  **📊 Insights** — Apresenta métricas e gráficos interativos para análise de desempenho.
3.  **🤖 Chatbot (IA + N8N)** — Oferece respostas automáticas a perguntas baseadas no conjunto de dados.
4.  **🧠 ML (Machine Learning)** — Implementa um modelo de regressão linear para previsão de vendas.
5.  **📋 Relatório Automático (YData-Profiling)** — Gera e exibe uma análise exploratória completa dos dados diretamente no navegador.
6.  **ℹ️ Sobre** — Contém informações sobre o projeto e dados para contato.

---

## 🚀 Próximos Passos

- Aprimorar os modelos de previsão de vendas com algoritmos mais avançados.
- Integrar os dashboards do Power BI diretamente na aplicação via API.
- Automatizar a geração de relatórios diários utilizando N8N.

---

## 💡 Contato

📧 **Email:** luisfilipemnovais@gmail.com  
💼 **LinkedIn:** [linkedin.com/in/luisfilipenovais](https://linkedin.com/in/luisfilipenovais)