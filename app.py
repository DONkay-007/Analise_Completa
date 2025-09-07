import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from calculations_limpo import df, format_number
import plotly.express as px

st.set_page_config(layout="wide")

st.title("DASHBOARD AGRO 🐂")

# Create tabs
aba1, aba2, aba3, aba4 = st.tabs(['Dataset', 'Insights', 'Chatbot', 'ML'])

# Tab 1: Dataset
with aba1:
    with st.container():
        st.subheader("📊 Dataset")

        filtro_cidade = st.sidebar.multiselect(
            "Cidade",
            options=df["cidade"].unique(),
            default=[],
            help="Selecione uma ou mais cidades para filtrar o dataset."
        )
        filtro_vendedor = st.sidebar.multiselect(
            "Vendedor",
            options=df["Vendedor"].unique(),
            default=[],
            help="Selecione um ou mais vendedores para filtrar o dataset."
        )

        filtered_df = df
        if filtro_cidade:
            filtered_df = filtered_df[filtered_df["cidade"].isin(filtro_cidade)]
        if filtro_vendedor:
            filtered_df = filtered_df[filtered_df["Vendedor"].isin(filtro_vendedor)]

        st.dataframe(filtered_df, use_container_width=True)

        st.write(f"**Total de registros exibidos**: {len(filtered_df)}")

# Tab 2: Insights (Placeholder)
with aba2:
    st.write("Insights content goes here")

# Tab 3: Chatbot (Placeholder)
with aba3:
    st.write("Chatbot content goes here")

# Tab 4: ML
with aba4:
    st.subheader("🤖 Previsão de Vendas com Machine Learning")

    # Features and Target
    X = df[['Estoque', 'Preco_kg']]
    y = df['Vendidos']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Model performance
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    # Layout with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Desempenho do Modelo")
        st.metric("R² (Acurácia)", f"{r2:.2f}", help="Indica que o modelo explica {r2:.0%} da variação nas vendas.")
        st.metric("RMSE (Erro Médio)", f"{rmse:.2f}", help="Previsões erram, em média, {rmse:.0f} unidades.")
        
        st.markdown("#### Impacto nas Vendas")
        st.write(f"**+1 unidade no estoque**: Vendas aumentam ~{model.coef_[0]:.1f} unidades")
        st.write(f"**+R$1 no preço/kg**: Vendas diminuem ~{abs(model.coef_[1]):.1f} unidades")

    with col2:
        st.markdown("#### Previsões vs. Reais")
        df_plot = pd.DataFrame({'Vendas Reais': y_test, 'Vendas Previstas': y_pred})
        chart = alt.Chart(df_plot).mark_circle(size=60, opacity=0.7).encode(
            x='Vendas Reais:Q',
            y='Vendas Previstas:Q',
            tooltip=['Vendas Reais', 'Vendas Previstas']
        ).interactive()
        line = alt.Chart(pd.DataFrame({'x': [0, y_test.max()], 'y': [0, y_test.max()]})).mark_line(color='red', strokeDash=[3,3]).encode(x='x', y='y')
        st.altair_chart(chart + line, use_container_width=True)

    # Manual Prediction
    st.markdown("---")
    st.subheader("🔮 Prever Vendas")
    estoque = st.number_input("Estoque disponível", min_value=0, value=100, step=10)
    preco = st.number_input("Preço por kg (R$)", min_value=0.0, value=10.0, step=0.5, format="%.2f")
    
    if st.button("Prever", type="primary"):
        pred = max(0, model.predict([[estoque, preco]])[0])
        st.success(f"Previsão: **{pred:.0f} unidades**")