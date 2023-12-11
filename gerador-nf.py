import pandas as pd
import argparse
from csv_json import criar_json
from csv_xml import criar_xml
from csv_yaml import criar_yaml

#importa o arquivo


parser = argparse.ArgumentParser(description='Gerador de saída  de NF em diferentes formatos')
parser.add_argument('--formato', choices=['xml', 'json', 'yaml'], required=True, help='Formato da saída (xml, json, yaml)')
parser.add_argument('--arquivo_csv', help='Caminho para o arquivo CSV dos produtos')

args = parser.parse_args()

caminho_arquivo = args.arquivo_csv
df = pd.read_csv(caminho_arquivo+'.csv')

if args.formato == 'xml':
        saida = criar_xml(df)
elif args.formato == 'json':
        saida = criar_json(df)
elif args.formato == 'yaml':
        saida = criar_yaml(df)



