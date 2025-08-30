#       Meus Passos seguidos Para obter insigths 📈📊🔍 Análise de Dados<br>

## 1 - Instalaçãoe e configuração do ambiente
## 2 - Importação dos dados
## 3 - Visualização dos dados
## 4 - Análise inicial dos dados
### Comandos básicos do pandas

- `df.head()` -> mostra os primeiros registros da tabela
- `df.tail()` -> mostra os últimos registros da tabela
- `df.info()` -> informações sobre a tabela (colunas, tipo de dado, valores nulos)
- `df.describe()` -> estatísticas descritivas das colunas numéricas
- `df.shape` -> número de linhas e colunas (linhas, colunas)
- `df.columns` -> lista os nomes das colunas
- `df.dtypes` -> tipos de dados de cada coluna
- `df.isnull().sum()` -> conta valores nulos em cada coluna
- `df['coluna']` -> seleciona uma coluna específica
- `df.groupby('coluna')` -> agrupa os dados por valores de uma coluna (útil para sumarizações)
- `df.sort_values('coluna')` -> ordena a tabela por uma coluna
- `df.dropna()` -> remove linhas com valores nulos
- `df.fillna(valor)` -> substitui valores nulos por um valor específico

## 5 - Tratamento e limpeza de dados

### Conversão de tipos de dados
- `pd.to_datetime(df['Data_de_vendas'], errors='coerce')`  
  Converte a coluna de datas para o tipo datetime.
- `pd.to_numeric(df['Estoque'], errors='coerce')`  
  Converte colunas numéricas para o tipo correto, permitindo valores nulos.

### Preenchimento de valores nulos
- `df['Data_venda'] = df['Data_venda'].fillna(df['Data_de_vendas'])`  
  Preenche datas faltantes em uma coluna usando valores da outra.
- `df['Estoque'] = df['Estoque'].fillna(df['Vendidos'])`  
  Preenche estoque faltante com o valor de vendidos.
- `df['Vendidos'] = df['Vendidos'].fillna(df['Estoque'])`  
  Preenche vendidos faltante com o valor de estoque.
- `df['Vendedor'] = df['Vendedor'].fillna('Desconhecido')`  
  Preenche vendedor faltante com o texto "Desconhecido".
- `df['Data_de_vendas'] = df['Data_de_vendas'].fillna(method='ffill')`  
  Preenche datas faltantes com o valor anterior.
- `df['Data_de_vendas'] = df['Data_de_vendas'].fillna(method='bfill')`  
  Preenche datas faltantes com o valor seguinte.
- `df['Data_de_vendas'] = df['Data_de_vendas'].fillna(pd.Timestamp('2023-01-01'))`  
  Preenche datas faltantes restantes com uma data padrão.
- Para linhas onde estoque e vendidos são ambos nulos:  
  `df.loc[mask, 'Estoque'] = 1` e `df.loc[mask, 'Vendidos'] = 1`

### Remoção e ajuste de colunas
- `df = df.drop(columns=['Data_venda'])`  
  Remove colunas redundantes após o tratamento.

### Criação e ajuste de colunas auxiliares
- Criação de colunas de localização (cidade, latitude, longitude) a partir de uma lista de cidades.
- Criação da coluna `Preco_kg` baseada em um dicionário de preços por produto.

### Exportação dos dados limpos
- `df.to_csv('data/banco_agro_projeto_limpo.csv', index=False)`  
  Salva o DataFrame



