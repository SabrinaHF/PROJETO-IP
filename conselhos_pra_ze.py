
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

url= 'https://api.adviceslip.com/advice'

def menu_principal():
    
    print('\n')
    print('~~~~~~ Cachaçaria do Seu Zé ~~~~~~')
    print('\n')
    print('      [ Conselhos Digitais ]')
    print('\n')
    print('          ==> Menu <==')
    print('\n')
    print(' 1. Quer tomar um ou mais conselhos, daqueles bem ligeiro?')
    print(' 2. Quer relembrar alguns conselhos véi? Apoi escolha esse aqui.')
    print(' 3. Quer ir simbora? Então tá certo...')
    print('\n')
    
    while True:
        try:
            opcao = int(input(' -> Me diga aqui a opção, homi: '))
            if opcao in [1, 2, 3]:
                break
            else:
                print('Errrouu! Opção inválida. Tente novamente, por favor.')
        except ValueError:
            print('Por favor, digite um número válido, vai.')
    
    return opcao

menu_principal()

def exibir_conselhos():


    print('\n')
    num = int(input(' -> Quer um conselho ou mais? Me diga quantos: '))
    print('\n')

    for i in range (num):
        consulta = requests.get(url)
        lista = consulta.json()
        conselho = lista["slip"]["advice"]
        print(f' >> Conselho nº {i+1}: {conselho}')
    
    print('\n')
    print(' -> Ê hein, achei profundo... tu achasse? Me diz lá embaixo.')
    print('\n')
    print(' 1. Entendi foi nada, traduz aí!')
    print(' 2. Guarde esses conselhos pra mim, robô!')
    print(' 3. Quero voltar lá no começo!')
    print('\n')
    escolha = int(input(' -> Digita aqui ó, a opção:'))
    
def main():

    while True:
        opcao = menu_principal()
        
        if opcao == 1:
            voltar_ao_menu = exibir_conselhos()
            if voltar_ao_menu:
                continue  
        elif opcao == 2:
            print("Aqui você pode mostrar conselhos antigos...")
        elif opcao == 3:
            print('Saindo... Até mais!')
            break  
        else:
            print('Opção inválida, tente novamente.')

main()

