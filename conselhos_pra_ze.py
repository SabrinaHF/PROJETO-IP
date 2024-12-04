# 1.0.Fazer menu:
#   1.1. Perguntar quantos conselhos Seu Zé quer receber (Ouvir o Seu Zé);
#   1.2. Exibir os conselhos mágicos da API na tela (consumir a API, ou seja, realizar requisições a um serviço web para obter ou enviar dados);
#   1.3. Dar a opção de salvar os conselhos em um arquivo de texto, junto com o ID do conselho;
#   1.4. Mostrar os conselhos guardados no arquivo de texto;
#   1.5. Traduzir os conselhos do inglês para o português - usar API deep_translator com o Google Translator;
#   1.6. Relembrar as dicas, permitindo que Seu Zé acesse os conselhos salvos e, se precisar, traduzi-los;
#        1.6.1. Opção de apenas traduzir o conselho da API
#        1.6.2. Opção de traduzir o que estiver salvo no arquivo de texto

import json
import requests
from deep_translator import GoogleTranslator
import os

url = 'https://api.adviceslip.com/advice'
arquivo_conselhos = 'conselhos_salvos.txt'


def menu_principal():
    print('\n')
    print('~~~~~~ Cachaçaria do Seu Zé ~~~~~~')
    print('\n')
    print('      [ Conselhos Digitais ]')
    print('\n')
    print('          ==> Menu <==')
    print('\n')
    print(' 1. Quer tomar um ou mais conselhos, daqueles bem ligeiro?')
    print(' 2. Quer relembrar alguns conselhos, véi? Apoi escolha esse aqui.')
    print(' 3. Quer ir simbora? Então tá certo...')
    print('\n')

    while True:
        try:
            opcao = int(input(' -> Me diga aqui a opção, homi: '))
            if opcao in [1, 2, 3]:
                break
            else:
                print('Errrouu! Opção inválida. Tenta de novo, com fé.')
        except ValueError:
            print('Vish, tem que ser um dos números.')

    if opcao == 1:
        opcao_um()
    elif opcao == 2:
        opcao_dois()
    else:
        print('\n')
        print("Até logo, véi! Volte sempre e vá pela sombra.")
        print('\n')

def opcao_um():
    print('\n')
    num = int(input(' -> Quer um conselho ou mais? Me diga quantos: '))
    print('\n')
    conselhos = []

    for i in range(num):
        consulta = requests.get(url)
        lista = consulta.json()
        conselho_id = lista["slip"]["id"]
        conselho = lista["slip"]["advice"]
        conselhos.append((conselho_id, conselho))
        print(f' >> Conselho nº {conselho_id}: {conselho}')

    print('\n')
    print(' -> Ê hein, achei profundo... tu achasse? Me diz lá embaixo.')
    print('\n')
    print(' 1. Entendi foi nada, traduz aí!')
    print(' 2. Adorei! Guarde esses conselhos pra mim, robô.')
    print(' 3. Quero voltar lá no começo!')
    print('\n')
    
    while True:
        try:
            escolha = int(input(' -> Digita aqui ó, a opção: '))
            if escolha in [1, 2, 3]:
                break
            else:
                print('Errrouu! Opção inválida. Tenta de novo, com fé.')
        except ValueError:
            print('Vish, tem que ser um dos números.')

    if escolha == 1:
        print('\n -> Traduzindo...')
        for id_, texto in conselhos:
            traduzido = traduzir_conselho(texto)
            print(f' >> Conselho nº {id_}: {traduzido}')
        
        
        print('\n 1. Entendi tudin! Me diga mais conselhos!')
        print(' 2. Tudo certo! Simbora para o menu!')
        
        while True:
            try:
                resposta_escolha = int(input('\n -> Diz aqui, rapidin, a opção: '))
                if resposta_escolha in [1, 2]:
                    break
                else:
                    print('Errrouu! Opção inválida. Tenta de novo, com fé.')
            except ValueError:
                print('Vish, tem que ser um dos números.')
        
        if resposta_escolha ==1:
            opcao_um()
        else:
            menu_principal()

    elif escolha == 2:
        salvar_conselhos(conselhos)
        print(' -> Só conselho da hora... Salvei tudo!')
        menu_principal()
    else:
        print(' -> E lá vamos nós!')
        menu_principal()

    
def opcao_dois():

    print('\n           ==> Os conselhos mais filé <==')
    print('\n')

    if not os.path.exists(arquivo_conselhos):
        print(' -> Eita, nenhum conselho salvo... Cuida!')
        menu_principal()
        return

    with open(arquivo_conselhos, 'r') as arquivo:
        conselhos = arquivo.readlines()

    for conselho in conselhos:
        print(f' >> {conselho.strip()}')

    print('\n')
    print(' -> Vish, tá em inglês. Quer traduzir? (s/n)')
    traduzir = input(' -> Me diga aqui: ').lower()
    if traduzir == 's':
        print('\n -> Traduzindo...')
        for conselho in conselhos:
            id_, texto = conselho.strip().split(": ", 1)
            traduzido = traduzir_conselho(texto)
            print(f' >> Conselho nº {id_}: {traduzido}')
    else:
        print(' -> Voltando ao menu principal...')

    menu_principal()

def salvar_conselhos(conselhos):
    print('\n -> Salvando conselhos...')
    with open(arquivo_conselhos, 'a') as arquivo:
        for id_, texto in conselhos:
            arquivo.write(f'{id_}: {texto}\n')
    

def traduzir_conselho(conselho):
    try:
        return GoogleTranslator(source='auto', target='pt').translate(conselho)
    except Exception as e:
        print(f'Deu ruim: {e}')
        return conselho


menu_principal()
