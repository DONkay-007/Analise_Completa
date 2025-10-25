# TODAS AS IMPORTAÇÔES USADAS ATÈ O MOMENTO
import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO
import time
import xlsxwriter
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.express as px
import matplotlib.pyplot as plt
import os
import requests
import json
from pathlib import Path
from datetime import datetime
import webbrowser
from ydata_profiling import ProfileReport

# ==========================
# Carregar dados
# ==========================

# Caminho do CSV
csv_path = "data/banco_agro_projeto_limpo.csv"
# ---------- VERIFICAÇÃO DO CSV ----------
if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
    df = pd.read_csv(csv_path)
else:
    st.error("❌ O arquivo CSV não foi encontrado ou está vazio. Verifique o caminho e os dados.")
    st.stop()  # interrompe o app se não houver CSV


# Padronizar nomes de colunas
df.columns = [c.strip() for c in df.columns]

# Converter para datetime mantendo suporte ao .dt
df["Data_de_vendas"] = pd.to_datetime(df["Data_de_vendas"])

# Salvar normalizado
df.to_csv("data/banco_agro_projeto_limpo.csv", index=False)

# ==========================
# Funções auxiliares
# ==========================
def format_number(value, prefix=''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'

def convert_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Dados")
    return output.getvalue()

def mensagem_sucesso():
    sucess = st.success('✅ Arquivo baixado com sucesso!')
    sucess.empty()

# ==========================
# Configuração da página
# ==========================
st.set_page_config(layout="wide")
st.title("📊 DASHBOARD AGRO 🐂")

# Criar abas
aba1, aba2, aba3, aba4, aba5, aba6= st.tabs(['📂 Dataset', '📈 Insights', '🤖 Chatbot', '🧠 ML','📋📌 Realatório','📚 Sobre'])

# ==========================
# Tab 1: Dataset
# ==========================
with aba1:
    with st.container():
        st.subheader("📊 Visualização do Dataset")

    # -----------------------------
    # FILTROS
    filtro_cidade = st.sidebar.multiselect(
        "🏙️ Cidade",
        options=df["cidade"].unique(),
        default=[]
    )
    filtro_vendedor = st.sidebar.multiselect(
        "🧑‍💼 Vendedor",
        options=df["Vendedor"].unique(),
        default=[]
    )
    with st.sidebar.expander('📅 Data da Compra'):
        data_compra = st.date_input(
            "Selecione o intervalo de datas",
            (df['Data_de_vendas'].min().date(), df['Data_de_vendas'].max().date())
        )

    # Aplicar filtros
    filtered_df = df.copy()
    if filtro_cidade:
        filtered_df = filtered_df[filtered_df["cidade"].isin(filtro_cidade)]
    if filtro_vendedor:
        filtered_df = filtered_df[filtered_df["Vendedor"].isin(filtro_vendedor)]
    if data_compra:
        inicio, fim = data_compra
        filtered_df = filtered_df[
            (filtered_df["Data_de_vendas"].dt.date >= inicio) &
            (filtered_df["Data_de_vendas"].dt.date <= fim)
        ]

    # Mostrar dados
    st.dataframe(filtered_df, use_container_width=True)
    st.markdown(f"**📌 Total de registros exibidos:** {len(filtered_df)}")

    # -----------------------------
    # DOWNLOAD
    coluna1, coluna2 = st.columns([3, 1])
    with coluna1:
        nome_arquivo = st.text_input('Digite o nome do arquivo (sem extensão):', key='nome_arquivo').strip()
    if not nome_arquivo:
        nome_arquivo = 'relatorio'
    if not nome_arquivo.lower().endswith('.xlsx'):
        nome_arquivo += '.xlsx'

    with coluna2:
        st.download_button(
            '⬇️ Baixar Excel',
            data=convert_excel(filtered_df),
            file_name=nome_arquivo,
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            on_click=mensagem_sucesso
        )






# ==========================
# Tab 2: Insights
# ==========================
with aba2:
    st.subheader("📊 Análises de Vendas")    
    coluna1, coluna2 = st.columns(2)

    # ---- Gráfico 1
    with coluna1:
        st.markdown("#### 📅 Faturamento por Total")
        df['Faturamento'] = df['Vendidos'] * df['Preco_kg']
        faturamento_total = df.groupby('Produto')['Faturamento'].sum().reset_index().round().sort_values(by="Faturamento", ascending=False)
        st.markdown(f"### |💰 Faturamento Total: **R$ {faturamento_total['Faturamento'].sum():,.2f}**|")
        
        
        st.markdown("#### 🌆 Faturamento por Cidade")
        df_cidade = df.groupby("cidade", as_index=False).agg({
            "Faturamento": "sum",   
            "Vendidos": "sum",      
            "latitude": "first",    
            "longitude": "first"    
        })
        fig = px.scatter_mapbox(
            df_cidade,
            lat="latitude",
            lon="longitude",
            size="Faturamento",
            color="Faturamento",
            hover_name="cidade",
            hover_data=["Vendidos", "Faturamento"],
            size_max=30,
            zoom=4
        )
        fig.update_layout(mapbox_style="carto-darkmatter", margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)

    # ---- Gráfico 2
    with coluna2:
        st.markdown("#### Perdas (Não vendidos)")
        df["Não_vendidos"] = df['Estoque'] * df["Preco_kg"]
        Perdas = df.groupby('Produto')['Não_vendidos'].sum().round(2).reset_index().sort_values(by="Não_vendidos",ascending=False)
        st.markdown(f"### |💸 Perdas Totais: **R$ {Perdas['Não_vendidos'].sum():,.2f}**|")
        
        
        st.markdown("#### 🧑‍💼 Faturamento por Vendedor")
        df_vendedor = df.groupby("Vendedor", as_index=False).agg({
            "Faturamento": "sum",    
            "Vendidos": "sum",      
            "latitude": "first",    
            "longitude": "first"  
        })
        fig = px.scatter_mapbox(
            df_vendedor,
            lat="latitude",
            lon="longitude",
            size="Faturamento",
            color="Faturamento",
            hover_name="Vendedor",
            hover_data=["Vendidos", "Faturamento"],
            size_max=30,
            zoom=4
        )
        fig.update_layout(mapbox_style="carto-darkmatter", margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
        
    st.markdown("---")
    
    # Colunas lado a lado: pizza e linha
    col3, col4 = st.columns(2)

   # ---- Gráfico 3: Pizza interativa (Plotly)
with col3:
    st.markdown("#### 👨‍💼 Rendimento de Funcionário")
    sales_maior = df.groupby('Vendedor')['Vendidos'].sum().reset_index().sort_values(by='Vendidos', ascending=False)

    fig_pizza = px.pie(
        sales_maior,
        names='Vendedor',
        values='Vendidos',
        color='Vendedor',
        color_discrete_sequence=px.colors.sequential.Viridis,
        hole=0.35,
    )
    fig_pizza.update_traces(
        textinfo='percent+label',
        pull=[0.05]*len(sales_maior),
        textfont_size=12
    )
    fig_pizza.update_layout(
        title=dict(text="🍕 Total Vendido por Vendedor", x=0.5, font=dict(size=18, color='#00c7c7')),
        paper_bgcolor='#0e1117',
        plot_bgcolor='#1e2130',
        font=dict(color='white', family="Arial"),
        height=400,
        margin=dict(t=60, b=20, l=0, r=0)
    )
    st.plotly_chart(fig_pizza, use_container_width=True)


# ---- Gráfico 4: Linhas interativas (Plotly)
with col4:
    st.markdown("#### 📈 Vendas Mensais por Ano (2024–2029)")

    df['Data_de_vendas'] = pd.to_datetime(df['Data_de_vendas'], errors='coerce')
    df_filtrado = df[df['Data_de_vendas'].dt.year.isin([2024, 2025, 2026, 2027, 2028, 2029])]
    df_filtrado['Ano'] = df_filtrado['Data_de_vendas'].dt.year
    df_filtrado['Mes'] = df_filtrado['Data_de_vendas'].dt.month
    vendas_mensais = df_filtrado.groupby(['Ano', 'Mes'], as_index=False)['Vendidos'].sum()

    fig_linha = px.line(
        vendas_mensais,
        x='Mes',
        y='Vendidos',
        color='Ano',
        markers=True,
        color_discrete_sequence=px.colors.sequential.Plasma
    )
    fig_linha.update_layout(
        title=dict(text="📊 Evolução de Vendas por Mês", x=0.5, font=dict(size=18, color='#00c7c7')),
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 13)),
            ticktext=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            title='Mês',
            showgrid=True,
            gridcolor='rgba(255,255,255,0.1)'
        ),
        yaxis=dict(title='Total Vendido', showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
        paper_bgcolor='#0e1117',
        plot_bgcolor='#1e2130',
        font=dict(color='white'),
        legend=dict(title='Ano', orientation='h', y=-0.2, x=0.5, xanchor='center'),
        height=400,
        margin=dict(t=60, b=50, l=40, r=20)
    )
    st.plotly_chart(fig_linha, use_container_width=True)
    st.markdown("---")
    
    def gerar_metricas():
        produto_mais = df['Produto'].mode()[0]
        yield f"📦 Produto mais vendido: **{produto_mais}**\n"
        time.sleep(0.5)

        media_estoque = df['Estoque'].mean()
        yield f"📊 Média de itens em estoque: **{media_estoque:.0f}**\n"
        time.sleep(0.5)

        media_vendas = df['Vendidos'].mean()
        yield f"🛒 Média de vendas: **{media_vendas:.0f}**\n"
        time.sleep(0.5)

        dispersao = df['Vendidos'].std() / df['Vendidos'].mean() * 100
        yield f"📉 Dispersão relativa das vendas: **{dispersao:.2f}%**\n"
        time.sleep(0.5)

        desvio = df['Vendidos'].std()
        yield f"📏 Desvio padrão das vendas: **{desvio:.0f}**\n"
        time.sleep(0.5)

        variancia = df['Vendidos'].var()
        yield f"🔎 Variância das vendas: **{variancia:.0f}**\n"
        time.sleep(0.5)

        faturamento_ano = df.groupby(df['Data_de_vendas'].dt.year)['Vendidos'].sum().reset_index()
        faturamento_ano.columns = ["Ano", "Total Vendido"]
        yield "📆 Vendas totais por ano: \n"
        yield faturamento_ano.to_string(index=False)
        time.sleep(0.5)

        faturamento_cidade = df.groupby("cidade")['Vendidos'].sum().reset_index()
        faturamento_cidade.columns = ["Cidade", "Total Vendido"]
        yield "🏙 Vendas totais por cidade:\n"
        yield faturamento_cidade.to_string(index=False)
        time.sleep(0.5)

    if st.button("🚀 Gerar Métricas"):
        st.write_stream(gerar_metricas)
        st.markdown("---")
        st.success("✅ Métricas geradas com sucesso!")
        
        
        
        
# ==========================
# Tab 3: Chatbot PROJETO AGRO
# ==========================

# URL do webhook (ajuste se necessário)
N8N_WEBHOOK_URL = "http://10.0.0.144:5678/webhook/chat-vendas"
with aba3:
    # ======= Estilo CSS =======
    st.markdown(
        """
        <style>
        .chat-container {
            background-color: #1e1e2f;
            color: white;
            padding: 20px;
            border-radius: 12px;
        }
        .chat-message { padding: 10px 14px; border-radius: 12px; margin-bottom: 10px; max-width:85%; font-size:14px;}
        .chat-user { background-color: #2e6fe2; color: white; margin-left:auto; }
        .chat-bot { background-color: #323449; color: #f1f1f1; margin-right:auto; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("🤖 Chatbot PROJETO AGRO")
    st.caption("Converse com seus dados agrícolas de forma inteligente 🌱")
    st.divider()
    st.markdown("### 📂 Envie ou selecione sua base de dados (CSV)")

    # Upload opcional do CSV
    uploaded_file = st.file_uploader("Envie o arquivo CSV com seus dados", type="csv")

    def ask_chatbot(question, uploaded_file=None):
        """
            Envia uma pergunta e um arquivo CSV (opcional) para o chatbot n8n e retorna a resposta.
        """
        try:
            csv_text = None

            # 1. Prioriza o arquivo enviado pelo usuário
            if uploaded_file is not None:
                raw_data = uploaded_file.getvalue()
                try:
                    # Tenta decodificar com UTF-8, o padrão mais comum
                    csv_text = raw_data.decode("utf-8")
                except UnicodeDecodeError:
                    # Se falhar, tenta com latin-1, comum em arquivos do Excel no Windows
                    print("Decodificação com UTF-8 falhou, tentando com latin-1.")
                    csv_text = raw_data.decode("latin-1", errors="replace")
            else:
                # 2. Se nenhum arquivo for enviado, procura por um arquivo local padrão
                possible_paths = [
                    Path("C:/n8n-ffmpeg/data/banco_agro_projeto_limpo.csv"), # Caminho Windows
                    Path("/data/banco_agro_projeto_limpo.csv"),             # Caminho Linux/Docker
                    Path("banco_agro_projeto_limpo.csv"),                   # Caminho relativo
                ]
                for p in possible_paths:
                    if p.exists():
                        print(f"Arquivo local encontrado em: {p}")
                        csv_text = p.read_text(encoding="utf-8", errors="replace")
                        break

            # Se, após todas as tentativas, nenhum CSV foi encontrado, retorna um erro
            if not csv_text:
                return "⚠️ Nenhum arquivo CSV encontrado. Por favor, envie um arquivo para continuar."

            # 3. Envia a requisição para o n8n
            payload = {"mensagem": question, "csv": csv_text}
            headers = {"Content-Type": "application/json"}

            resp = requests.post(N8N_WEBHOOK_URL, json=payload, headers=headers, timeout=60) # Timeout aumentado para 60s
            resp.raise_for_status() # Lança um erro para respostas HTTP 4xx/5xx

            # 4. Processa a resposta do n8n de forma simplificada e segura
            try:
                data = resp.json()
                # Acessa a chave "resposta" de forma segura com .get()
                # Se a chave não existir, retorna None e a mensagem de erro é acionada
                resposta = data.get("resposta")
                if resposta:
                    return resposta
                return f"🤷 Resposta recebida, mas em formato inesperado: {json.dumps(data)[:500]}"

            except ValueError: # Ocorre se a resposta não for um JSON válido
                return f"❌ Erro de decodificação: A resposta do n8n não é um JSON válido. Resposta recebida: {resp.text[:400]}"

        except requests.exceptions.ConnectionError:
            return "🚫 Erro de conexão com o n8n. Verifique se o endereço do webhook está correto e se o n8n está em execução."
        except requests.exceptions.Timeout:
            return "⏱️ Tempo de espera excedido. O n8n demorou muito para responder (mais de 60 segundos)."
        except requests.exceptions.HTTPError as e:
            # Tenta extrair o corpo da resposta de erro para mais detalhes
            body = e.response.text if e.response else "Nenhum detalhe adicional."
            return f"❌ Erro HTTP {e.response.status_code}: {e} - {body[:800]}"
        except Exception as e:
            # Captura qualquer outro erro inesperado
            return f"⚠️ Um erro inesperado ocorreu: {type(e).__name__}: {e}"

    # ======= Sessão de mensagens =======
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.markdown("### 💬 Conversa")

    chat_container = st.container()
    with chat_container:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for msg in st.session_state.messages:
            role_class = "chat-user" if msg["role"] == "user" else "chat-bot"
            st.markdown(
                f'<div class="chat-message {role_class}">{msg["content"]}</div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    # ======= Entrada do usuário =======
    user_query = st.chat_input("Digite sua pergunta aqui...")

    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.spinner("💭 Pensando..."):
            response = ask_chatbot(user_query, uploaded_file=uploaded_file)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

    # ======= Rodapé =======
    st.divider()
    st.info(f"🌐 Chat conectado ao n8n: `{N8N_WEBHOOK_URL}`")
    st.caption("🧠 Desenvolvido com n8n + Streamlit + Gemini 2.5 Flash")
    st.caption(datetime.now().strftime("Última atualização: %d/%m/%Y %H:%M"))
# ==========================



    # Tab 4: ML
with aba4:
    st.subheader("👾⚡ Previsão de Vendas com Machine Learning")

    # Features e alvo
    X = df[['Estoque', 'Preco_kg']]
    y = df['Vendidos']

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Modelo
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Métricas
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    # Layout com 2 colunas
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📊 Desempenho do Modelo")
        st.metric("R² (Acurácia)", f"{r2:.2f}", help=f"Indica que o modelo explica {r2:.0%} da variação nas vendas.")
        st.metric("RMSE (Erro Médio)", f"{rmse:.2f}", help=f"Previsões erram, em média, {rmse:.0f} unidades.")
        
        st.markdown("#### 📌 Impacto nas Vendas")
        st.write(f"**+1 unidade no estoque** → vendas aumentam em média ~{model.coef_[0]:.1f} unidades")
        st.write(f"**+R$1 no preço/kg** → vendas diminuem em média ~{abs(model.coef_[1]):.1f} unidades")

    with col2:
        st.markdown("#### 🔍 Previsões vs. Reais")
        import matplotlib.pyplot as plt  # garante que plt foi importado
        fig, ax = plt.subplots()
        ax.scatter(y_test, y_pred, alpha=0.7, s=60)
        ax.plot([0, y_test.max()], [0, y_test.max()], color="red", linestyle="--")
        ax.set_xlabel("Vendas Reais")
        ax.set_ylabel("Vendas Previstas")
        ax.set_title("Vendas Reais vs. Previstas")
        st.pyplot(fig)

    # -----------------------------
    st.markdown("---")
    st.subheader("🔮 Prever Vendas")

    estoque = st.number_input("📦 Estoque disponível", min_value=0, value=100, step=10)
    preco = st.number_input("💰 Preço por kg (R$)", min_value=0.0, value=10.0, step=0.5, format="%.2f")
    
    if st.button("Prever", type="primary"):
        pred = max(0, model.predict([[estoque, preco]])[0])
        st.success(f"✅ Previsão de vendas: **{pred:.0f} unidades**")
        st.info(f"Com um estoque de {estoque} unidades e preço de R${preco:.2f}/kg")
        





# ==========================
# 📋📌 ABA 5 - RELATÓRIO AUTOMÁTICO (GERA E ABRE LOCAL)
# ==========================
with aba5:
    st.subheader("📋📌 Geração de Relatório Automático com YData-Profiling")
    st.write("Faça o upload de um arquivo (CSV ou Excel) para gerar e abrir um relatório completo de análise exploratória.")

    uploaded_file = st.file_uploader(
        "Escolha um arquivo CSV ou Excel", 
        type=['csv', 'xlsx'],
        key="profiling_uploader"
    )

    if uploaded_file is not None:
        try:
            with st.spinner("📂 Carregando dados..."):
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)

            st.success("✅ Dados carregados com sucesso! Gerando relatório...")

            # Caminho do arquivo local
            report_path = "profiling_report.html"

            with st.spinner("🔍 Analisando o conjunto de dados... Isso pode levar alguns segundos."):
                profile = ProfileReport(df, title="Relatório de Análise Exploratória", explorative=True)
                profile.to_file(report_path)

            st.success("✅ Relatório gerado com sucesso!")
            st.markdown(f"O relatório foi salvo em: `{report_path}`")

            # Botão para abrir o relatório automaticamente no navegador local
            if st.button("🌐 Abrir relatório no navegador"):
                webbrowser.open_new_tab(f"file://{os.path.abspath(report_path)}")
                st.info("O relatório foi aberto em uma nova aba do seu navegador.")

        except Exception as e:
            st.error(f"❌ Ocorreu um erro ao processar o arquivo: {e}")

    else:
        st.info("Aguardando o upload de um arquivo para começar a análise.")




# ==========================
# Tab 6: Sobre o Projeto Agro
# ==========================
with aba6:
    st.subheader("📚 Sobre o Projeto Agro")
    st.markdown("""
    Bem-vindo ao Dashboard Agro! Este projeto foi desenvolvido para fornecer insights valiosos sobre vendas agrícolas, utilizando análise de dados, visualizações interativas e modelos de machine learning.

    ### Objetivos do Projeto
    - Analisar dados de vendas agrícolas para identificar tendências e padrões.
    - Fornecer ferramentas interativas para explorar os dados.
    - Implementar um chatbot inteligente para responder perguntas sobre os dados.
    - Utilizar machine learning para prever vendas futuras com base em variáveis-chave.

    ### Tecnologias Utilizadas
    - **Streamlit**: Framework principal para construção do dashboard.
    - **Pandas & NumPy**: Manipulação e análise de dados.
    - **Plotly & Matplotlib**: Visualizações interativas e estáticas.
    - **Scikit-learn**: Modelagem preditiva com machine learning.
    - **n8n**: Automação de workflows e integração do chatbot.

    ### Equipe de Desenvolvimento
    - Desenvolvedor 1: [Luís Filipe Moreira Novais]
    - Analista de Dados: [Luís Filipe Moreira Novais]

    ### Contato
    Para dúvidas, sugestões ou colaborações, entre em contato através do email: luisfilipemnovais@gmail.com
    """)
    st.subheader("🛠️ Ferramentas Futuras")
    st.markdown("""
    - 📊 Análises avançadas com mais gráficos interativos
    - 🤖 Chatbot aprimorado com mais funcionalidades
    - 🧠 Modelos de ML adicionais para diferentes previsões
    - 🌐 Integração com APIs externas para dados em tempo real
    - 📥 Opções de exportação adicionais (PDF, CSV)
    - 🔒 Segurança e autenticação de usuários
    """)
    st.info("🚧 Esta seção está em desenvolvimento. Fique atento para futuras atualizações!")