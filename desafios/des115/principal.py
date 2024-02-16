#Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções, cadastrar uma nova pessoa, listar todas as pessoas cadastradas.
from time import sleep
import lib.interface as intr
import lib.arquivo as ar

arq = 'cursoemvideo.txt'

if not ar.arquivoExiste(arq):
    ar.criarArquivo(arq)
while True:
    resposta = intr.menu(['Ver pessoas cadastradas','Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        ar.lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa
        intr.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = intr.leiaInt('Idade: ')
        ar.cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do Sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção inválida!')
    sleep(1)
