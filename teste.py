print("Olá Mundo!!!")
VALOR = 5.5
NOME = 'João'
print(VALOR)
print(type(VALOR))
print(type(NOME))

def diga_ola():
    #O que faz o diga ola
    print('Olá ' + input("Qual seu nome: ") + '\nidade: ' + str(VALOR+10))

diga_ola()
