# 🧭 Guia de Desenvolvimento e Extração de Insights 📈📊🔍

## 🧩 Etapas Seguidas

### 1️⃣ Instalação e Configuração
```bash
pip install pandas numpy streamlit sweetviz matplotlib seaborn plotly scikit-learn
```

---

### 2️⃣ Importação e Visualização dos Dados
```python
df.head()
df.info()
df.describe()
```

---

### 3️⃣ Limpeza e Transformação (ETL)
```python
df['Data_de_vendas'] = pd.to_datetime(df['Data_de_vendas'], errors='coerce')
df['Vendedor'].fillna('Desconhecido', inplace=True)
df.drop(columns=['Data_venda'], inplace=True)
```

---

### 4️⃣ Criação de Novas Métricas
```python
df['Faturamento'] = df['Vendidos'] * df['Preco_kg']
ranking_produtos = df.groupby('Produto')['Faturamento'].sum().sort_values(ascending=False)
```

---

### 5️⃣ Análise Exploratória (EDA)
```python
import sweetviz as sv
report = sv.analyze(df)
report.show_html("sweetviz_report.html", open_browser=True)
```

---

### 6️⃣ Implementação no Streamlit
- **Dataset:** Tabela filtrável e download.  
- **Insights:** KPIs e visualizações.  
- **Chatbot:** Integração com N8N.  
- **ML:** Previsão de vendas via `LinearRegression`.  
- **Relatório:** YData-Profiling aberto em `localhost:8501`.

---

### 7️⃣ Exportação Final
```python
df.to_csv('data/banco_agro_projeto_limpo.csv', index=False)
```

---

## 🧠 Tecnologias
🐍 Python · 📊 Pandas · 📈 Matplotlib · 🤖 Streamlit · 🧮 Scikit-Learn · 📘 YData-Profiling · 🔄 N8N

---

## 🧾 Resultado Final
- Dashboard interativo completo.  
- Relatórios automáticos locais.  
- Pipeline de dados limpo e escalável.

