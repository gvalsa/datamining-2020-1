var1 = 50

var2 = 100

produto = var1 * var2

# Prioridade de Operações

#  ^ (Potência)
# * /  ( Mult e div )
# + -

conta = (var1 + var2) * var2
print(conta)

def faz_conta():
    return 0

print(faz_conta())

def oi():
  print("oi")

oi()
x = faz_conta()

def soma_dois_valores(valor1, valor2):
    return valor1 + valor2

x = soma_dois_valores( 3 ,4 )
print(x)

x = soma_dois_valores(2 , 8)
print(x)

def raiz_cubica():

 x = 4
 print(x)

def div_por_seis(valor):
    return ((valor % 2) == 0) and ((valor % 3) == 0)

print(div_por_seis(9))
print(div_por_seis(12))

def e_par(valor):
    return(valor % 2) == 0

def testes ():
    print(div_por_seis(9))
    print(div_por_seis(12))

def teste_par():
    valor = input('Insira um número: ')
    if e_par(int(valor)) == True:
        print('é par pai')

teste_par()

def dez_mult_tres():
    """ Imprime os primeiros 10 numeros nao negativos multiplos de 3"""

    cont = 0
    numero = 1
    while cont < 10:
        if numero % 3 == 0:
         print(numero)
         cont = cont + 1
        numero = numero + 1  # numero = numero + 1

dez_mult_tres()

