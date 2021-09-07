#It's a module created with some functions in order to make the main program more clean
from time import sleep
lista = []


def arquivoexiste(arq):
    try:
        a = open(arq, 'rt')
    except:
        print(f'ERRO! O arquivo {arq} não foi encontrado')
        sleep(1)
        print(f'Vamos criar um novo arquivo...')
        try:
            a = open(arq, 'wt+')
            a.close()
        except:
            print('Erro ao criar o arquivo!')
        else:
            sleep(1)
            print(f'Arquivo {arq} criado com sucesso!')
    else:
        a = open(arq, 'rt')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'Erro ao tentar ler o arquivo {nome}')
    else:
        print(f'{"COD":^3}{"NOME":^17}{"IDADE":^5}')
        sleep(0.5)
        cont = 0
        for linha in a:
            dados=linha.split(";")
            dados[1] = dados[1].replace("\n", '')
            print(f'{cont:^3}{dados[0]:^17}{dados[1]:^5}')
            cont+=1
            lista.append(dados[:])
            dados.clear()
            sleep(0.5)
    finally:
        a.close()


def titulo(txt):
    print("-"*50)
    print(f'{txt:^50}')
    print("-"*50)


def menu(*elements):
    for c in range(1, len(elements)+1):
        print(f"[{c}] - {elements[c-1]}")


def desejacontinuar(txt):
    while True:
        try:
            desejo = input(txt).strip().upper()[0]
            if desejo not in 'SN':
                print('resposta inválida! Tente novamente!')
        except:
            print("Ocorreu algum erro com os dadso inseridos")

        else:
            return desejo


def novocadastro(arq, nome = '<desconhecido>', idade = 0):
    while True:
        # nome do cadastrado
        while True:
            nome = input('Digite o nome: ').strip().upper()
            if nome.isnumeric():
                print('Digite o nome, não um número!')
            else:
                break
        # idade do cadastrado
        while True:
            try:
                idade = int(input('Digite a idade: '))
            except:
                print('Dado inválido. Tente Novamente!')
            else:
                break
        print(f'Você digitou as seguinte informações: \nNome: {nome} \nIdade: {idade}')
        # confirmação de dados
        while True:
            conf = input('Deseja cadastrar com os dados fornecidos[S/N]? ').strip().upper()[0]
            if conf not in 'SN':
                print('Resposta inválida!')
            #CONFIRMANDO OS DADOS SE INICIA A ADIÇÃO DOS DADOS NO ARQUIVO
            elif conf in 'S':
                try:
                    a = open(arq, 'at')
                except:
                    print(f'Erro ao tentar abrir no arquivo {arq} no cadastro')
                else:
                    try:
                        a.write(f'{nome};{idade}\n')
                    except:
                        print(f'Erro ao tentar escrever no arquivo {arq}')
                    else:
                        sleep(1)
                        print(f'Novo registro de {nome} cadastrados com sucesso!')
                        a.close()
                break
            #SE NÃO CONFIRMAR INFORMA O NºAO CADASTRO E VAI PARA CONTINUAR
            elif conf in 'N':
                print('OK, dados NÃO cadastrados')
                sleep(1)
                break
        #Deseja continuar?
        if conf in 'SN':
            resp = desejacontinuar('Deseja continuar cadastrando [S/N]? ')
            if resp in 'N':
                break


def escolhacadastrado():
    while True:
        try:
            print('-' * 30)
            escolha = int(input('Qual o código dó elemento que deseja ver os dados? '))
        except:
            print('Dado fornecido não é válido')
        else:
            if escolha > len(lista) - 1:
                print(f'Não encontramos alguem com o código {escolha}. Tente '
                      f'novamente!')
            else:
                print(f'No código {escolha} está registrado:')
                print(f'{lista[escolha][0]} com '
                      f'{lista[escolha][1]} anos')
            print('-' * 30)
            resp = desejacontinuar('Deseja ver mais algum cadastro[S/N]? ')
            if resp in 'N':
                print('voltando...')
                lista.clear()
                sleep(1)
                print('-' * 50)
                break

