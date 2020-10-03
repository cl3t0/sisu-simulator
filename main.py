from datetime import datetime
from classificacao import calcula_classificacao, salva_classificacao


def main():

    arquivo_entrada = open('entrada.txt', 'r')
    quantidade_cursos, quantidade_alunos = arquivo_entrada.readline().split()
    quantidade_cursos = int(quantidade_cursos)
    quantidade_alunos = int(quantidade_alunos)
    cursos = le_cursos(arquivo_entrada, quantidade_cursos)
    alunos = le_alunos(arquivo_entrada, quantidade_alunos)
    classificacao = calcula_classificacao(cursos, alunos)
    salva_classificacao(classificacao)
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

        nome = linha_1[0]
        data = linha_1[1] + linha_1[2] + linha_1[3]
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
        return (x['nota_media'], x['notas'][0], x['data'])

    alunos = sorted(
        alunos, reverse=True, key=ordem)

    return alunos


main()