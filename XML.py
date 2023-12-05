import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom import minidom


df = pd.read_csv("produtos.csv")



def criar_xml(df, caminho_arquivo):
    # Cria o elemento raiz
    root = ET.Element('Produtos')

    # Adiciona elementos filho
    for i in range(len(df)):
        produto = ET.SubElement(root, "produto")
        nome = ET.SubElement(produto, "nome")
        nome.text = df['nome'].iloc[i]
        preco = ET.SubElement(produto, "preco")
        preco.text = str(df['preco'].iloc[i])
        quantidade = ET.SubElement(produto, "quantidade")
        quantidade.text = str(df['quantidade'].iloc[i])
        marca = ET.SubElement(produto, "marca")
        marca.text = str(df['marca'].iloc[i])
        cod_barras = ET.SubElement(produto, "cod_barra")
        cod_barras.text = str(df['cod_barra'].iloc[i])
        imposto = ET.SubElement(produto, "imposto")
        imposto.text = str(df['imposto'].iloc[i])
        

    # Cria a árvore XML
    tree = ET.ElementTree(root)

    # Escreve o arquivo XML
    xml_string = ET.tostring(root, encoding='utf-8').decode('utf-8')
    xml_formatted = minidom.parseString(xml_string).toprettyxml(indent="    ") 
    
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(xml_formatted)

    print(f'Arquivo {caminho_arquivo} criado com sucesso')
#Teste
criar_xml(df, 'arquivo_xml.xml')