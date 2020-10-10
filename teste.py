from main import main
import os

QUANTIDADE = len(os.listdir('testes'))

for i in range(1, QUANTIDADE+1):
    main(f'testes/teste{i}/entrada.txt', f'testes/teste{i}/saida.txt')
    saida = open(f'testes/teste{i}/saida.txt', 'r')
    saida_esperada = open(f'testes/teste{i}/saida_esperada.txt')
    saida_texto = saida.read()
    saida_esperada_texto = saida_esperada.read()
    if saida_texto == saida_esperada_texto:
        print(f"Teste {i}: OK!")
    else:
        print(f"Teste {i}: FALHOU!")