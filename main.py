from datetime import datetime
from classificacao import calcula_classificacao, salva_classificacao


def main(nome_entrada, nome_saida):

    arquivo_entrada = open(nome_entrada, 'r')
    quantidade_cursos, quantidade_alunos = arquivo_entrada.readline().split()
    quantidade_cursos = int(quantidade_cursos)
    quantidade_alunos = int(quantidade_alunos)
    cursos = le_cursos(arquivo_entrada, quantidade_cursos)
    alunos = le_alunos(arquivo_entrada, quantidade_alunos)
    classificacao = calcula_classificacao(cursos, alunos)
    salva_classificacao(classificacao, nome_saida)
    arquivo_entrada.close()


def le_cursos(arquivo, quantidade):
    cursos = []
    for i in range(quantidade):

        linha = arquivo.readline().split(',')

        codigo = int(linha[0])
        nome = linha[1]
        vagas = int(linha[2])

        curso = {
            'codigo': codigo,
            'nome': nome,
            'vagas': vagas
        }

        cursos.append(curso)
    return cursos


def le_alunos(arquivo, quantidade):
    alunos = []
    for i in range(quantidade):
        linha_1 = arquivo.readline().split()
        linha_2 = arquivo.readline().split()

        nome = ""
        for texto in linha_1[:-3]:
            nome += texto + " "
        nome = nome[:-1]
        data = linha_1[-3] + linha_1[-2] + linha_1[-1]
        data = datetime.strptime(data, '%d/%m/%Y-%H:%M:%S')

        nota_redacao = int(linha_2[0])
        nota_matematica = int(linha_2[1])
        nota_linguagens = int(linha_2[2])
        codigo_opcao_1 = int(linha_2[3])
        codigo_opcao_2 = int(linha_2[4])
        nota_media = round(
            (nota_redacao + nota_matematica + nota_linguagens)/3, 2)

        aluno = {
            'nome': nome,
            'data': data,
            'notas': (nota_redacao, nota_matematica, nota_linguagens),
            'nota_media': nota_media,
            'codigo_opcoes': (codigo_opcao_1, codigo_opcao_2)
        }

        alunos.append(aluno)

    def ordem(x):
        return (-x['nota_media'], -x['notas'][0], x['data'])

    alunos = sorted(
        alunos, key=ordem)

    return alunos