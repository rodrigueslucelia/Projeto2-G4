## Projeto Gerador de Arquivos

- O código lê um arquivo csv que gera três tipos de arquivos: XML, JSON e YAML, para realizar a conversão o input deverá ser:
 
- Se a saída for em XML, posso chamar o programa com python gerador-nf.py –formato=xml --arquivo_csv "nome_do_seu_arquivo"
 
- Se a saída for em JSON, posso chamar o programa com python gerador-nf.py —formato=json "nome_do_seu_arquivo"
 
- Se a saída for em JSON, posso chamar o programa com python gerador-nf.py —formato=yaml "nome_do_seu_arquivo"


## Bibliotecas necessárias:

```http
 pip install pandas
```

```http
 pip install pyyaml 
```

```http
 pip install minidom
```

### Importar Bibliotecas

```http
 import pandas as pd
 import argparse
 from json import loads, dumps
```

```http
 import yaml
 import xml.etree.ElementTree as ET
 from xml.dom import minidom
```
