import requests, pandas as pd, os

os.makedirs("data/raw", exist_ok=True)

url = "https://api.worldbank.org/v2/country/br/indicator/NY.GDP.MKTP.CD?format=json&date=2010:2020"
resp = requests.get(url)
data = resp.json()[1] 

df = pd.DataFrame(data)
df = df[['date', 'value']].rename(columns={'date':'ano','value':'pib'})
df.to_csv("data/raw/anp_dados.csv", index=False)

print("✅ Dados de PIB extraídos com sucesso!")
