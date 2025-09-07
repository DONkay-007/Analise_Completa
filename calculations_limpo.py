# calculations.py
import pandas as pd

# Carrega apenas o DF pronto (exportado no notebook)
df = pd.read_csv("data/banco_agro_projeto_limpo.csv")

# Opcional: padronizar nomes
df.columns = [c.strip() for c in df.columns]

df.to_csv("data/banco_agro_projeto_limpo.csv", index=False)

def format_number(value, prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'

