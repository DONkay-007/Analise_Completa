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

---

## ⚙️ Como Executar o Projeto

Fico feliz que tenha interesse em rodar meu projeto! Para facilitar, preparei um guia rápido para você configurar o ambiente e executar a aplicação.

### **Pré-requisitos**

Antes de começar, certifique-se de que possui:
*   **Python 3.8 ou superior** ([Download](https://www.python.org/downloads/))
*   **Git** ([Download](https://git-scm.com/downloads))

### **Passo a Passo**

### **1. Clone o Repositório**

Abra seu terminal e execute os comandos abaixo.

```bash
git clone https://github.com/LuisF-08/Analise_Completa.git
cd Analise_Completa
```

## **2. Crie e Ative um Ambiente Virtual**

Isso mantém as dependências do projeto isoladas e evita conflitos.

### *   **No Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### *   **No macOS e Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### **3. Instale as Dependências**

Com o ambiente virtual ativado, use o arquivo `requirements.txt` que preparei para instalar todas as bibliotecas de uma só vez(obs: não são todos eles que utilizei no projeto mas é bom colocar pois ele podem ser usados em atualizações futuras).

    ```bash
    pip install -r requirements.txt
    ```

### **4. Rodando o Projeto**

Tudo pronto! Inicie o dashboard interativo com o comando:

    ```bash
    streamlit run app.py
    ```

automaticamente irá abrir uma aba em seu navegador, use com sabedoria😁.
