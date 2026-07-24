# estrutura dos dados
from menu import menu_numerado, limpar_tela
from classes import pilhas_ou_filas

def adicionar_elemento():
    """ função global para adicionar elementos 
    independente do tipo de lista """

    while True:
        entrada = input('Qual elemento deseja adicionar: ')
        if entrada == '' or not entrada.strip():
            print('\n[ERRO] Espaços vazios não são permitidos!\n')
            continue
        else:
            print(f'O elemento [{entrada}] foi adicionado ✔️\n')
            break

    return entrada

def remover_elemento():
    pass

lista_pilhas = []
lista_filas = []

def rodar_programa():

    while True:
        limpar_tela()
        opcao = menu_numerado()
        match opcao:
            case 1:
                
                pilha_ou_fila = pilhas_ou_filas()
                elemento = adicionar_elemento()

                if pilha_ou_fila == 1:
                    lista_pilhas.append(elemento)
                else:
                    lista_filas.append(elemento)

            case 2 :
                pass

            case 3:
                pass

            case 4:
                print('\nprograma encerrado.\n')
                break

rodar_programa()