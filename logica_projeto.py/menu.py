def ler_opcao_numerica():
    pass

def menu_numerado():

    opcoes = ['Adicionar elemento', 'Remover elemento', 'Ver estado atual', 'Encerrar'] # <- lista criada apenas para exibição dinâmica

    print('-'*30)
    for indice, opcao in enumerate(opcoes, start=1):
        print(f'{indice} - {opcao}') # <- esse bloco foi feito do jeito que está apenas para
    print('-'*30)                   #  poupar espaço e não ter que lotar o inicio da função de 'prints'

    while True:
        
        try:
            opcao = int(input('O que deseja fazer -> '))
        except ValueError:  # <- esse bloco é responsável por conferir uma entrada numérica
            print('[ERRO] valor inválido\n')
            continue

        if (opcao < 1 or 
            opcao > 4): # <- esse bloco confere se o usuário digitou algo dentre as opções sugeridas antes de retornar o valor da função
            print('[ERRO] opção não encontrada\n')
            continue
        else:
            break

    opcoes = ['Pilhas', 'Filas']

    print('\nCom o que deseja trabalhar:')
    for indice, lista in enumerate(opcoes, start=1):
        print(f'{indice} - {lista}')

    while True:

        try:
            pilha_ou_fila = int(input('Selecione uma opção -> '))
        except ValueError: 
            print('[ERRO] valor inválido\n')
            continue

        if (pilha_ou_fila < 1 or
            pilha_ou_fila > 2):
            print('[ERRO] opção não encontrada\n')
            continue
        else:
            break

    return opcao, pilha_ou_fila

menu_numerado()