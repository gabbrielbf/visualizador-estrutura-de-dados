# estrutura dos dados
from menu import menu_numerado, limpar_tela

opcao, pilha_ou_fila = menu_numerado()

def trabalhar_pilhas(lista_pilhas):
    pass

def adicionar_elemento():


    while True:
        entrada = input('Qual elemento deseja adicionar: ')
        if entrada == '' or not entrada.strip():
            print('\n[ERRO] Espaços vazios não são permitidos!\n')
            continue
        else:
            print(f'O elemento [{entrada}] foi adicionado ✔️\n')
            break

    return entrada

lista_pilhas = []
lista_filas = []

while True:
    limpar_tela()
    menu_numerado()
    match opcao:
        case 1:
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
