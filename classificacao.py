def calcula_classificacao(cursos, alunos):
    classificacoes = {}
    nao_selecionados_primeira_opcao = []
    for curso in cursos:
        nome = curso['nome']
        selecionados, lista_espera = selecionar_alunos_primeira_opcao(
            curso, alunos)
        if len(selecionados) != 0:
            classificacao = {
                'nota_corte': selecionados[-1]['nota_media'],
                'selecionados': selecionados,
                'lista_espera': lista_espera
            }
        else:
            classificacao = {
                'nota_corte': 0,
                'selecionados': [],
                'lista_espera': []
            }
        classificacoes[nome] = classificacao
        for i in lista_espera:
            if i not in nao_selecionados_primeira_opcao:
                nao_selecionados_primeira_opcao.append(i)
    for curso in cursos:
        nome = curso['nome']
        selecionados, lista_espera = selecionar_alunos_segunda_opcao(
            curso, nao_selecionados_primeira_opcao, classificacoes[nome])
        classificacoes[nome]['selecionados'] += selecionados
        if len(selecionados) != 0:
            classificacoes[nome]['nota_corte'] = selecionados[-1]['nota_media']
        classificacoes[nome]['lista_espera'] += lista_espera
    return classificacoes


def selecionar_alunos_segunda_opcao(curso, alunos, classificacao):
    nome = curso['nome']
    vagas = curso['vagas']
    codigo = curso['codigo']
    alunos_segunda_opcao = []
    for aluno in alunos:
        segunda_opcao = aluno['codigo_opcoes'][1]
        if segunda_opcao == codigo:
            alunos_segunda_opcao.append(aluno)
    if len(classificacao['selecionados']) == vagas:
        return [], alunos_segunda_opcao
    else:
        vagas_restantes = vagas - len(classificacao['selecionados'])
        selecionados = alunos_segunda_opcao[:vagas_restantes]
        lista_espera = alunos_segunda_opcao[vagas_restantes:]
        return selecionados, lista_espera


def selecionar_alunos_primeira_opcao(curso, alunos):
    codigo = curso['codigo']
    alunos_primeira_opcao = []
    for aluno in alunos:
        primeira_opcao = aluno['codigo_opcoes'][0]
        if primeira_opcao == codigo:
            alunos_primeira_opcao.append(aluno)

    if len(alunos_primeira_opcao) == 0:
        return [], []
    else:
        vagas = curso['vagas']
        selecionados = alunos_primeira_opcao[:vagas]
        lista_espera = alunos_primeira_opcao[vagas:]
        return selecionados, lista_espera


def salva_classificacao(classificacoes, nome_arquivo):
    arquivo = open(nome_arquivo, 'w')
    for nome in classificacoes.keys():
        classificacao = classificacoes[nome]
        nota_corte = classificacao['nota_corte']
        selecionados = classificacao['selecionados']
        lista_espera = classificacao['lista_espera']
        arquivo.write(f"{nome} {nota_corte}\n")
        arquivo.write('Selecionados\n')
        for i in selecionados:
            arquivo.write(f"{i['nome']} {i['nota_media']}\n")
        arquivo.write("Lista de Espera\n")
        for i in lista_espera:
            arquivo.write(f"{i['nome']} {i['nota_media']}\n")
        arquivo.write('\n')
    arquivo.close()