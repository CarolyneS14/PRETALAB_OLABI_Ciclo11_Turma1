
import csv
import random
from datetime import datetime, timedelta

# Construindo a função
# coloque todo o código que anterior numa função que receba o nome e quantidade de linhas do arquivo com extensão csv
def meu_arquivo(nome_arquivo, num_linhas):
  colunas = ['data_internacao', 'tratamento', 'dias_internacao', 'custo_total']
  tratamento = ['cirurgia', 'tratamento_intensivo', 'exames', 'fisioterapia']
  data_inicial = datetime.now() - timedelta(days=730)

  with open(nome_arquivo, 'w', newline='') as arquivo:
    construtor = csv.writer(arquivo)
    #adicionar a lista criada chamada coluna como cabeçalho do arquivo csv
    construtor.writerow(colunas)

    for _ in range(num_linhas):
      data_internacao = data_inicial + timedelta(days=random.randint(1, 730))
      tratamento = random.choice(tratamento)
      dias_internacao = random.randint(1, 30)
      custo_total = round(random.uniform(100.0, 10000.0), 2)
      construtor.writerow([data_internacao.strftime('%Y-%m-%d'), tratamento, dias_internacao, custo_total])
      