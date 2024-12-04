
# 1.0.Fazer menu:
#   1.1. Perguntar quantos conselhos Seu Zé quer receber (Ouvir o Seu Zé);
#   1.2. Exibir os conselhos mágicos da API na tela (consumir a API, ou seja, realizar requisições a um serviço web para obter ou enviar dados);
#   1.3. Dar a opção de salvar os conselhos em um arquivo de texto, junto com o ID do conselho;
#   1.4. Mostrar os conselhos guardados no arquivo de texto;
#   1.5. Traduzir os conselhos do inglês para o português - usar API deep_translator com o Google Translator;
#   1.6. Relembrar as dicas, permitindo que Seu Zé acesse os conselhos salvos e, se precisar, traduzi-los;
#        1.6.1. Opção de apenas traduzir o conseho da API
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
    opcao = int(input(' -> Me diga aqui a opção, homi: '))

    if opcao == 1:
        opcao_um()
    elif opcao == 2:
        opcao_dois()
    elif opcao == 3:
        print("Até logo, véi! Volte sempre.")
    else:
        print("Opção inválida. Tente novamente.")
        menu_principal()


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
        print(f' >> Conselho nº {i + 1}: {conselho}')

    print('\n')
    print(' -> Ê hein, achei profundo... tu achasse? Me diz lá embaixo.')
    print('\n')
    print(' 1. Entendi foi nada, traduz aí!')
    print(' 2. Eu entendi foi tudo, pois sou troglodita... digo, poliglota. Guarde esses conselhos pra mim, robô.')
    print(' 3. Quero voltar lá no começo!')
    print('\n')
    escolha = int(input(' -> Digita aqui ó, a opção:'))

    if escolha == 1:
        for _, texto in conselhos:
            traduzido = traduzir_conselho(texto)
            print(f' >> Traduzido: {traduzido}')
    elif escolha == 2:
        salvar_conselhos(conselhos)
    elif escolha == 3:
        menu_principal()
    else:
        print("Opção inválida. Voltando ao menu principal.")
        menu_principal()


def opcao_dois():
    print('\n -> Relembrando conselhos salvos...')
    if not os.path.exists(arquivo_conselhos):
        print(' -> Nenhum conselho salvo ainda.')
        return

    with open(arquivo_conselhos, 'r') as arquivo:
        conselhos = arquivo.readlines()

    for conselho in conselhos:
        print(f' >> {conselho.strip()}')

    print('\n')
    print(' -> Quer traduzir os conselhos salvos? (s/n)')
    traduzir = input(' -> Responda aqui: ').lower()
    if traduzir == 's':
        for conselho in conselhos:
            _, texto = conselho.strip().split(": ", 1)
            traduzido = traduzir_conselho(texto)
            print(f' >> Traduzido: {traduzido}')
    else:
        print(' -> Voltando ao menu principal...')
        menu_principal()


def salvar_conselhos(conselhos):
    print('\n -> Salvando conselhos...')
    with open(arquivo_conselhos, 'a') as arquivo:
        for id_, texto in conselhos:
            arquivo.write(f'{id_}: {texto}\n')
    print(' -> Conselhos salvos com sucesso!')


def traduzir_conselho(conselho):
    try:
        return GoogleTranslator(source='auto', target='pt').translate(conselho)
    except Exception as e:
        print(f'Erro ao traduzir: {e}')
        return conselho


menu_principal()
