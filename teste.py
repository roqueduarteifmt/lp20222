print("Olá Mundo!!!")
valor = 5.5
nome = 'João'
print(valor) 
print(type(valor))
print(type(nome))

def digaOla():
    print('Olá ' + input("Qual seu nome: ") + '\nidade: ' + str(valor+10))

digaOla()