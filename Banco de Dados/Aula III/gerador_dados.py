
import random
import csv
# Função para gerar nomes de alunos fictícios
def gerar_alunos(qtd_alunos):
    alunos = []
    for i in range(1, qtd_alunos + 1):
        nome = f'Aluno {i:03}'
        matricula = f'2023{i:04}'
        alunos.append((nome, matricula))
    return alunos

# Função para gerar disciplinas fictícias
def gerar_disciplinas():
    return [
        ('Matemática',),
        ('Português',),
        ('História',),
        ('Geografia',),
        ('Ciências',)
    ]


    # Função para gerar notas aleatórias para os alunos
def gerar_notas(qtd_alunos, qtd_disciplinas):
    notas = []
    for aluno_id in range(1, qtd_alunos + 1):
        for disciplina_id in range(1, qtd_disciplinas + 1):
            nota = round(random.uniform(5.0, 10.0), 1)
            notas.append((aluno_id, disciplina_id, nota))
    return notas


# Função para salvar os dados em CSV
def salvar_csv(nome_arquivo, colunas, dados):
    with open(nome_arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(colunas)
        writer.writerows(dados)
    print(f'Dados salvos em {nome_arquivo}')


# Geração de dados fictícios
def gerar_dados_ficticios(qtd_alunos):
    # Gerar dados
    alunos = gerar_alunos(qtd_alunos)
    disciplinas = gerar_disciplinas()
    notas = gerar_notas(qtd_alunos, len(disciplinas))

    # Salvar em arquivos CSV
    salvar_csv('alunos.csv', ['nome', 'matricula'], alunos)
    salvar_csv('disciplinas.csv', ['nome'], disciplinas)
    salvar_csv('notas.csv', ['id_aluno', 'id_disciplina', 'nota'], notas)
