import pandas as pd
from json import loads, dumps

df = pd.read_csv("produtos.csv")
produtos = df.to_json(orient="records")
parsed = loads(produtos)
arq_jason = dumps(parsed, indent = 2)

with open('arquivo_json', 'w') as arquivo:
  arquivo.write(arq_jason)
