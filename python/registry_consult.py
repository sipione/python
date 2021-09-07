#lib which was useful for the main program
import cadastro
from time import sleep

#research an archive for registration, if it doesn't exists a new one is create automatically
arq = 'cadastrados.txt'
cadastro.arquivoexiste(arq)

#Main program
cadastro.titulo("SISTEMA DE CADASTROS")
while True:
    cadastro.menu("Cadastrar Novo", "Ver resumo", "Busca de cadastrados", "Sair do sistema")
    try:
        resp = int(input('Qual a sua escolha? '))
    except:
        print('O valor introduzido não é válido, tente novamente!')
    else:
        if resp > 4 or resp < 1:
            print('Só existem 4 opções, escolha de 1 a 4!')
            print('-'*50)
            sleep(2)
        elif resp == 1:
            cadastro.titulo("NOVO REGISTRO")
            print('Cadastrando um novo elemento...')
            sleep(1.5)
            cadastro.novocadastro(arq)
        elif resp == 2:
            sleep(1)
            cadastro.titulo("ELEMENTOS CADASTRADOS")
            cadastro.lerarquivo(arq)
            cadastro.lista.clear()
            print('Esse é a lista de cadastrados!')
            print('-'*50)
            sleep(2)
        elif resp == 3:
            cadastro.titulo("BUSCA INDIVIDUAL")
            print('Buscando dados no sistema...')
            sleep(1)
            cadastro.lerarquivo(arq)
            cadastro.escolhacadastrado()
        elif resp == 4:
            print('Saindo do sistema...')
            sleep(1.5)
            break

print('<< Obrigado! >>')
