import pandas as pd
import sqlite3

# Lê o CSV
df = pd.read_csv('data/processed/anp_tratado.csv')

# Cria o banco SQLite
conn = sqlite3.connect('data/processed/anp.db')

# Salva os dados na tabela 'anp'
df.to_sql('anp', conn, if_exists='replace', index=False)

# Fecha conexão
conn.close()
