
import csv
import math
from datetime import datetime

# Funcao para carregar arquivos csv
def carregar_dados(nome_arquivo):
  dados = []
  with open(nome_arquivo, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
      dados.append(linha)
  return dados  
  