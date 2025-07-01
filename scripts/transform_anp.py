import pandas as pd, os

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv("data/raw/anp_dados.csv")

df['pib_milhoes'] = df.pib / 1e6  # converte o valor para milhões
df.to_parquet("data/processed/anp_tratado.parquet", index=False)

print("✅ Dados de PIB transformados com sucesso!")
