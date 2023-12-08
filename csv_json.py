import pandas as pd
from json import loads, dumps

def criar_json(df):
    
    produtos = df.to_json(orient="records")
    parsed = loads(produtos)
    arq_jason = dumps(parsed, indent = 2)

    with open('arquivo_json', 'w') as arquivo:
      arquivo.write(arq_jason)
    print('Arquivo JSON criado') 
    return 
