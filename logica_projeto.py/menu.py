import os, time

def ler_opcao_numerica():
    """ função responsável por retornar uma opção numérica sem haver
    necessidade de ficar tratando cada try e except inteiro separadamente """

    while True:
        try:
            return int(input('Escolha uma dentre as opções acima -> '))
        except ValueError:
            print('[ERRO] opção não encontrada\n')
            continue

def limpar_tela():
    """ limpa a tela para manter a interface organizada """

    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_numerado():
    """ função responsável pela exibição do menu numerado 
    e pelo retorno das opções para funcionamento do programa """

    opcoes = ['Adicionar elemento', 'Remover elemento', 'Ver estado atual', 'Encerrar'] # <- lista criada apenas para exibição dinâmica

    print('-'*30)
    for indice, opcao in enumerate(opcoes, start=1):
        print(f'{indice} - {opcao}') # <- esse bloco foi feito do jeito que está apenas para
    print('-'*30)                   #  poupar espaço e não ter que lotar o inicio da função de 'prints'

    while True:
        
        opcao = ler_opcao_numerica()

        if (opcao < 1 or 
            opcao > 4): # <- esse bloco confere se o usuário digitou algo dentre as opções sugeridas antes de retornar o valor da função
            print('[ERRO] opção não encontrada\n')
            continue
        else:
            break

    return opcao

def pilhas_ou_filas():
    """ função separada para definir o tipo de lista a ser trabalhada """

    opcoes = ['Pilhas', 'Filas'] # <- lista criada apenas para exibição dinâmica
    
    print('\nCom o que deseja trabalhar:')
    print('-'*30)
    for indice, lista in enumerate(opcoes, start=1):
        print(f'{indice} - {lista}')
    print('-'*30)

    while True:

        pilha_ou_fila = ler_opcao_numerica()

        if (pilha_ou_fila < 1 or
            pilha_ou_fila > 2): # <- esse bloco de while true serve apenas para definir qual será o caminho traçado pelo usuário após
            print('[ERRO] opção não encontrada\n') # decidir qual opção dentre as opções, a partir daqui saberemos se ele quer trabalhar com pilhas ou filas
            continue
        else:
            break

    return pilha_ou_fila