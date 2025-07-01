import pandas as pd

df = pd.read_parquet('data/processed/anp_tratado.parquet')
df.to_csv('data/processed/anp_tratado.csv', index=False)
