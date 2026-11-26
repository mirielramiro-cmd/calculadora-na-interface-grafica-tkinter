import tkinter as tk
#Criando Janela Principal
janela_principal = tk.Tk()
janela_principal.geometry('640x480')
janela_principal.title('Calculadora')
#Definindo as funções.
def alterar1(i):
    global numero_atual
    numero_atual += str(numeros[i])
    visor_numero.config(text=numero_atual)

def alterar2(j):
    global numero_antigo, numero_atual, r, clique, contagem
    numero_antigo = numero_atual
    visor_numero.config(text=numero_antigo)
    for k in range(len(botoes_numeros)):
        botoes_numeros[k].config(command = lambda k=k: alterar3(k))
    match j:
        case 0:
            r = 0
        case 1:
            r = 1
        case 2:
            r = 2
        case 3: 
            r = 3
    if clique > contagem:
        clique = 0
        match r:
            case 0:
                visor_numero.config(text=float(numero_antigo)*2)
                numero_atual = str(float(numero_antigo)*2)
            case 1:
                visor_numero.config(text=float(0))
                numero_atual = '0'
            case 2:
                visor_numero.config(text=float(numero_antigo)*float(numero_antigo))
                numero_atual = float(numero_antigo)*float(numero_antigo)
            case 3:
                if numero_antigo != 0:
                    visor_numero.config(text='1')
                    numero_atual = '1'
                else:
                    visor_numero.config(text='Erro')
                    numero_atual =''
                    numero_antigo=''
    else:
        contagem = clique
        clique +=1
def alterar3(i):
    global numero_atual, numero_antigo
    numero_atual = ''
    numero_atual += str(numeros[i])
    visor_numero.config(text=numero_atual)


def resultar():
    global numero_atual, numero_antigo, r, clique, contagem
    clique = 0
    contagem = 0
    if numero_atual != '' and numero_antigo != '':
        match r:
                case 0:
                    numero_atual = str(float(numero_atual) + float(numero_antigo))
                    visor_numero.config(text=numero_atual)
                case 1:
                    numero_atual = str(float(numero_antigo) - float(numero_atual))
                    visor_numero.config(text=numero_atual)
                case 2:
                    numero_atual = str(float(numero_antigo)*float(numero_atual))
                    visor_numero.config(text=numero_atual)
                case 3:
                    if float(numero_atual) !=0:
                        numero_atual = str(float(numero_antigo)/float(numero_atual))
                        visor_numero.config(text=numero_atual)
                    else:
                        visor_numero.config(text='Erro')
                        numero_atual = ''
                        numero_antigo = ''
    else:
        visor_numero.config(text='Erro')
        numero_atual = ''
        numero_antigo = ''

#Dividindo a janela em dois frames e as variáveis que vamos usar.
visor = tk.Frame(janela_principal)
visor.pack()
calculador = tk.Frame(janela_principal)
calculador.pack()
visor_numero = tk.Label(visor, text= 0)
visor_numero.pack(pady = 10)
botoes_numeros = []
numeros = ['0','1','2','3','4','5','6','7','8','9']
r = 0
botoes_operadores = []
numero_atual = ''
numero_antigo = ''
clique = 0
contagem = 0
#Criando os botões

botao_zero = tk.Button(calculador, text= '0', command = lambda i=0: alterar1(0), width = 20, height =5)
botao_zero.grid(row = 3, column = 1)
botoes_numeros.append(botao_zero)

for i in range(9):
    botao = tk.Button(calculador, text=i+1,command = lambda i=i: alterar1(i+1), width = 20, height = 5)
    botao.grid(row = i//3, column = i%3)
    botoes_numeros.append(botao)
#Criaremos os botões de operadores e depois a lógica para calculadora.

botao_soma = tk.Button(calculador, text= '+', command = lambda i=0: alterar2(0), width = 20, height = 5)
botao_soma.grid(row = 3, column = 3 )
botoes_operadores.append(botao_soma)

botao_subtracao = tk.Button(calculador, text= '-', command = lambda j=1: alterar2(1), width = 20, height = 5)
botao_subtracao.grid(row= 2, column = 3)
botoes_operadores.append(botao_subtracao)

botao_multiplicacao = tk.Button(calculador, text= '*', command = lambda j=2: alterar2(2), width = 20, height = 5)
botao_multiplicacao.grid(row= 1,column =3)
botoes_operadores.append(botao_multiplicacao)

botao_divisao = tk.Button(calculador, text= '/', command = lambda j=3: alterar2(3),width = 20, height = 5)
botao_divisao.grid(row=0, column = 3)
botoes_operadores.append(botao_divisao)

botao_igualdade = tk.Button(calculador,text='=',command = resultar, width = 20, height =5)
botao_igualdade.grid(row=3, column=2)

#Definido os botões e as variáveis número atual e número antigo, faremos a lógica da calculadora.

janela_principal.mainloop()