import pandas as pd 
import yaml


def criar_yaml(df):
    dic = pd.DataFrame.to_dict(df, orient = "records")
    dic
    with open('arquivo_yaml', 'w') as arquivo:
      yaml.dump(dic, arquivo)
    print('Arquivo YAML criado')
    return 