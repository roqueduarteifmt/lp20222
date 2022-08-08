#1. Faça um programa que imprima o seu nome.
print('João Paulo Delgado Preti')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
print(30*27)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
print((5+8+12)/3)

#4. Faça um programa que leia e imprima um número inteiro.
numero = int(input('Digite um número: '))
print(numero)

#5. Faça um programa que leia dois números reais e os imprima.
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
print(str(numero1) + ' ' + str(numero2))

#6. Faça um programa que leia um número inteiro e imprima o seu antecessor e o seu sucessor.
print (f'Antecessor de {numero}: {numero-1}')
print (f'Sucessor de {numero}: {numero+1}')

#7. Faça um programa que leia o nome o endereço e o telefone de um cliente e ao final, imprima esses dados.
nome = input ('Nome: ')
endereco = input ('Endereço: ')
telefone = input ('Telefone: ')
print(f'\nNome: {nome}\nEndereço: {endereco}\nTelefone: {telefone}\n')

#8. Faça um programa que leia dois números inteiros e imprima a subtração deles.
print(f'Subtração de {numero1} por {numero2} = {numero1 - numero2}')

#9. Faça um programa que leia umnúmero real e imprima ¼ deste número.
print(numero/4)

#10. Faça um programa que leia três números reais e calcule a média aritmética destes números. Ao final, o programa deve imprimir o resultado do cálculo.
numero3 = float(input('Digite o terceiro número: '))
print((numero1+numero2+numero3)/3)

#11. Faça um programa que leia dois números reais e calcule as quatro operações básicas entre estes dois números, adição, subtração,multiplicação e divisão. Ao final, o programa deve imprimir os resultados dos cálculos.
print(f'{numero1} + {numero2} = {numero1+numero2}')
print(f'{numero1} - {numero2} = {numero1-numero2}')
print(f'{numero1} * {numero2} = {numero1*numero2}')
print(f'{numero1} / {numero2} = {numero1/numero2}')

#12. Faça um programa que leia um número real e calcule o quadrado deste número. Ao final, o programa deve imprimir o resultado do cálculo.
print(numero1**2)

#13. Faça um programa que leia o saldo de uma conta poupança e imprima o novo saldo, considerando um reajuste de 2%.
print(f'{numero} + 2% = {numero*1.02}')

#14. Faça um programa que leia a base e a altura de um retângulo e imprima o perímetro (base + altura) e a área (base * altura).
base = float(input('Informe a base do retângulo: '))
altura = float(input('Informe a altura do retângulo: '))
print(f'Perímetro do retângulo: {base + altura}')
print(f'Área do retângulo: {base * altura}')

#15. Faça um programa que leia o valor de um produto, o percentual do desconto desejado e imprima o valor do desconto e o valor do produto subtraindo o desconto.
valor_produto = float(input('Valor do produto: '))
percentual_desconto = int(input('Percentual de desconto: '))
print(f'Valor do desconto: {valor_produto*percentual_desconto/100}')
print(f'Valor final do Produto: {valor_produto-valor_produto*percentual_desconto/100}')

#16. Faça um programa que calcule o reajuste do salário de um funcionário. Para isso, o programa deverá ler o salário atual do funcionário e ler o percentual de reajuste. Ao final imprimir o valor do novo salário.
salario = float(input('Salário: '))
reajuste = int(input('Reajuste (%): '))
print(f'Salário reajustado: R$ {salario*(1+reajuste/100)}')

#17. Faça um programa que calcule a conversão entre graus centígrados e Fahrenheit. Para isso, leia o valor em centígrados e calcule com base na fórmula a seguir. Após calcular o programa deve imprimir o resultado da conversão.
#F = (9 x C +160) / 5
celsius = float(input('Temperatura (Celsius): '))
fahrenheit = (9 * celsius + 160) / 5
print(f'{celsius} graus celsius equivale a {fahrenheit} graus farenheit.')

#18. Faça umprograma que calcule a quantidade de litros de combustível consumidos em uma viagem, sabendo-se que o carro tem autonomia de 12 km por litro de combustível. O programa deverá ler o tempo decorrido na viagem e a velocidade média e aplicar as fórmulas:
#D = T x V       L = D / 12
#Em que:
#• D = Distância percorrida em horas
#• T = Tempo 
#• V = Velocidade média
#• L = Litros de combustível consumidos
#Ao final, o programa deverá imprimir a distância percorrida e a quantidade de litros consumidos na viagem.
tempo = int(input('Duração da viagem em minutos: '))
velocidade = int(input('Velocidade média (km/h): '))
distancia = velocidade*tempo/60
print(f'Distância percorrida: {distancia} km')
print(f'Litros gastos: {distancia/12}')

#19. Faça um programa que calcule o valor de uma prestação em atraso. Para isso, o programa deve ler o valor da prestação vencida, a taxa periódica de juros e o período de atraso. Ao final, o programa deve imprimir o valor da prestação atrasada, o período de atraso, os juros que serão cobrados pelo período de atraso, o valor da prestação acrescido dos juros. Considere juros simples.
prestacao = float(input('Valor da prestação atrasada: '))
dias_atraso = int(input('Qtde de dias de atraso: '))
juros_diario = float(input('Juros diário (%): '))
print(f'Valor da prestação com multa: R$ {prestacao * (1+dias_atraso*juros_diario/100)}')

#20. Faça um programa que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). Para isso, será necessário também ler o valor da cotação do dólar.
dolar = float(input('US$: '))
cotacao = float(input('Cotação: R$ '))
print(f'R$ {dolar*cotacao}')
