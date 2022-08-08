import this
import Operacoes #Acessando a classe operações
this.opcao = -1 #Declaração de variável global
this.num1  = 0
this.num2  = 0

def mostrarMenu():
    print('Escolha uma das opções abaixo: \n' +
          '1. Soma\n'                         +
          '2. Subtração\n'                    +
          '3. Multiplicação\n'                +
          '4. Divisão\n'                      +
          '0. Sair\n\n')
    this.opcao = int(input())#Entrada de dados

def coletarNum1():
    print('Informe o primeiro número: ')
    this.num1 = float(input()) #Convertendo um texto em número com vírgula

def coletarNum2():
    print('Informe o segundo número: ')
    this.num2 = float(input())#Convertendo um texto em número com vírgula

def executar():
    while(this.opcao != 0):
        mostrarMenu() #Chamando o método que mostra opções para o usuário

        if this.opcao == 1:
            coletarNum1() #Pegando o primeiro número