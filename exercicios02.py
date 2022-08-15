'''
Exercícios sobre os comandos de condição em python
'''

from datetime import date, datetime

TODAY = datetime.now()

def main():
    '''
    Executa todos os exercícios resolvidos
    '''
    #1. Faça um programa que leia dois valores numéricos inteiros e efetue
    #   a adição, caso o resultado seja maior que 10, apresentá-lo.
    valor1 = int(input('Valor1: '))
    valor2 = int(input('Valor2: '))
    adicao = valor1 + valor2
    if adicao > 10:
        print(adicao)

    #2. Faça um programa que leia dois valores inteiros e efetue a adição.
    #   Caso o valor somado seja maior que 20, este deverá ser apresentado
    #   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
    #   20, este deverá ser apresentado subtraindo-se 5.
    valor1 = int(input('Valor1: '))
    valor2 = int(input('Valor2: '))
    adicao = valor1 + valor2
    if adicao > 20:
        print(adicao + 8)
    else:
        print(adicao - 5)    

    #3. Faça um programa que leia um número e imprima uma das duas mensagens:
    #   "É múltiplo de 3"ou "Não é múltiplo de 3".
    valor1 = int(input('Valor1: '))
    if valor1 % 3 == 0:
        print('É múltiplo de 3')
    else:
        print('Não é múltiplo de 3')

    #4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
    valor1 = int(input('Valor1: '))
    if valor1 % 5 == 0:
        print('É divisível por 5')
    else:
        print('Não é divisível por 5')

    #5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
    valor1 = int(input('Valor1: '))
    if valor1 % 3 == 0 and valor1 % 7 == 0:
        print('É divisível por 3 e 7')
    else:
        print('Não é divisível por 3 e 7')

    #6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
    #   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
    #   bruto. Faça um programa que permita entrar com o salário bruto
    #   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
    salario_bruto = float(input('Salário Bruto: '))
    valor_prestacao = float(input('Valor da Prestação: '))
    if valor_prestacao > (salario_bruto * 0.3):
        print('Empréstimo não autorizado')
    else:
        print('Empréstimo autorizado')

    #7. Faça um programa que leia um número e indique se o número está compreendido
    #   entre 20 e 50 ou não.
    valor1 = int(input('Valor1: '))
    if valor1 >= 20 and valor1 <= 50:
        print('Número está entre 20 e 50')
    else:
        print('Número não está entre 20 e 50')

    #8. Faça um programa que leia um número e imprima uma das mensagens:
    #   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
    valor1 = int(input('Valor1: '))
    if valor1 > 20:
        print('Número maior do que 20')
    elif valor1 < 20:
        print('Número menor do que 20')
    else:
        print('Número igual a 20')

    #9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
    #   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
    #   verificar se o ano de nascimento informado é válido.
    valor1 = int(input('Ano de Nascimento: '))
    if (valor1 >= 1900 and valor1 < TODAY.year):
        print(f'Idade: {TODAY.year - valor1} anos')
    else:
        print('Ano de nascimento inválido!')

    #10. Faça um programa que leia três números inteiros e imprima os três em ordem
    #    crescente.
    valor1 = int(input('Valor1: '))
    valor2 = int(input('Valor2: '))
    valor3 = int(input('Valor3: '))
    if valor1 < valor2 and valor1 < valor3:
        if valor2 < valor3:
            print(f'{valor1} {valor2} {valor3}')
        else:
            print(f'{valor1} {valor3} {valor2}')    
    if valor2 < valor1 and valor2 < valor3:
        if valor1 < valor3:
            print(f'{valor2} {valor1} {valor3}')
        else:
            print(f'{valor2} {valor3} {valor1}')
    if valor3 < valor1 and valor3 < valor2:
        if valor1 < valor2:
            print(f'{valor3} {valor1} {valor2}')
        else:
            print(f'{valor3} {valor2} {valor1}')

    #11. Faça um programa que leia 3 números e imprima o maior deles.
    valor1 = int(input('Valor1: '))
    valor2 = int(input('Valor2: '))
    valor3 = int(input('Valor3: '))
    maior_valor = valor1
    if valor2 > maior_valor:
        maior_valor = valor2
    if valor3 > maior_valor:
        maior_valor = valor3
    print(f'Maior valor: {maior_valor}')

    #12. Faça um programa que leia a idade de uma pessoa e informe:
    #• Se é maior de idade
    #• Se é menor de idade
    #• Se é maior de 65 anos
    valor1 = int(input('Idade: '))
    if valor1 > 65:
        print('Maior de 65')
    elif valor1 >= 18:
        print('Maior de idade')
    else:
        print('Menor de idade')

    #13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
    #    da prova [2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
    #    a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
    #    "Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
    #    reprovação e as demais em prova final).
    nome = input('Nome do aluno: ')
    nota1 = round(float(input('Nota 1: ')), 1)
    nota2 = round(float(input('Nota 2: ')), 1)
    media = round((nota1 + nota2) / 2, 1)
    situacao = ''
    if media >= 7:
        situacao = 'Aprovado'
    elif media >= 3:
        situacao = 'Prova Final'
    else:
        situacao = 'Reprovado'
    print(nome)
    print('NOTA1\tNOTA2\tMEDIA\tSITUACAO')
    print(f'{nota1}\t{nota2}\t{media}\t{situacao}')

    #14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
    #    desconto do INSS segundo a tabela seguir:
    #Salário Faixa de Desconto
    #Menor ou igual à R$600,00 Isento
    #Maior que R$600,00 e menor ou igual a R$1200,00 20%
    #Maior que R$1200,00 e menor ou igual a R$2000,00 25%
    #Maior que R$2000,00 30%
    salario_bruto = float(input('Salário: '))
    desconto_inss = 0.0
    if salario_bruto > 2000:
        desconto_inss = salario_bruto * 0.3
    elif salario_bruto > 1200:
        desconto_inss = salario_bruto * 0.25
    elif salario_bruto > 600:
        desconto_inss = salario_bruto * 0.2
    else:
        desconto_inss = 0.0
    print(f'Desconto do INSS: R$ {round(desconto_inss, 2)}')

    #15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
    #    valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
    #    Faça um programa que leia o valor do produto e imprima o valor da venda.
    custo = float(input('Valor do produto: '))
    venda = 0.0
    if custo < 20:
        venda = custo * 1.45
    else:
        venda = custo * 1.3
    print(f'Valor de venda: R$ {round(venda, 2)}')

    #16. A confederação brasileira de natação irá promover eliminatórias para o
    #    próximo mundial. Faça um programa que receba a idade de um nadador e imprima
    #    a sua categoria segundo a tabela a seguir:
    #Categoria Idade
    #Infantil A 5 - 7 anos
    #Infantil B 8 - 10 anos
    #Juvenil A 11 - 13 anos
    #Juvenil B 14 - 17 anos
    #Sênior maiores de 18 anos
    idade = int(input('Idade: '))
    if idade >= 18:
        print('Sênior')
    elif idade >= 14:
        print('Juvenil B')
    elif idade >= 11:
        print('Juvenil A')
    elif idade >= 8:
        print('Infantil B')
    else:
        print('Infantil A')

    #17. Depois da liberação do governo para as mensalidades dos planos de saúde,
    #    as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
    #    muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
    #    Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
    #    nome e o valor que ela deverá pagar.
    #Idade Valor
    #Até 10 anos R$30,00
    #Acima de 10 até 29 anos R$60,00
    #Acima de 29 até 45 anos R$120,00
    #Acima de 45 até 59 anos R$150,00
    #Acima de 59 até 65 anos R$250,00
    #Maior que 65 anos R$400,00
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    valor = 0.0
    if idade > 65:
        valor = 400
    elif idade > 59:
        valor = 250
    elif idade > 45:
        valor = 150
    elif idade > 29:
        valor = 120
    elif idade > 10:
        valor = 60
    else:
        valor = 30
    print(f'Nome: {nome}\tIdade: {idade}\tValor: R$ {round(valor, 2)}')

    #18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
    #    correspondente. Caso o usuário digite um número fora desse intervalo, deverá
    #    aparecer uma mensagem informando que não existe mês com este número.
    mes = int(input('Mês: '))
    if mes < 1 or mes > 12:
        print('Mês Inválido!!!')
    else:
        data = datetime(2022,mes,1)
        print(data.strftime('%b'))

    #19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
    #    para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
    #    mesmo número de pontos, criar um programa que informe se uma equipe foi
    #    classificada, de acordo com a seguinte especificação:
    #• Ler os pontos obtidos por cada jogador da equipe;
    #• Mostrar esses valores em ordem decrescente;
    #• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
    #  caso contrário, imprimir a mensagem "Equipe desclassificada".
    valor1 = int(input('Pontos Jogador 1: '))
    valor2 = int(input('Pontos Jogador 2: '))
    valor3 = int(input('Pontos Jogador 3: '))
    if valor1 > valor2 and valor1 > valor3:
        if valor2 > valor3:
            print('{valor1} {valor2} {valor3}')
        else:
            print('{valor1} {valor3} {valor2}')   
    if valor2 > valor1 and valor2 > valor3:
        if valor1 > valor3:
            print('{valor2} {valor1} {valor3}')
        else:
            print('{valor2} {valor3} {valor1}')
    if valor3 > valor1 and valor3 > valor2:
        if valor1 > valor2:
            print('{valor3} {valor1} {valor2}')
        else:
            print('{valor3} {valor2} {valor1}')
    pontos = valor1 + valor2 + valor3
    if pontos > 100:
        print(f'Média de pontos: {round(pontos/3, 1)}')
    else:
        print('Equipe desclassificada')

    #20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
    #    acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
    #    de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
    #    O programa deve imprimir uma mensagem informando o saldo médio e o valor de
    #    crédito.
    #Saldo Médio Percentual
    #de 0 a 500 nenhum crédito
    #de 501 a 1000 30% do valor do saldo médio
    #de 1001 a 3000 40% do valor do saldo médio
    #acima de 3001 50% do valor do saldo médio
    saldo_medio = float(input('Saldo médio: R$ '))
    credito = 0.0
    if saldo_medio > 3001:
        credito = saldo_medio * 0.5
    elif saldo_medio > 1001:
        credito = saldo_medio * 0.4
    elif saldo_medio > 501:
        credito = saldo_medio * 0.3
    else:
        credito = 0.0
    print(f'Crédito: R$ {round(credito, 2)}')

    #21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
    #    livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
    #    imprimir um recibo conforme mostrado a seguir. Considerar que o professor
    #    tem dez dias para devolver o livro e o aluno só três dias.
    #• Nome do livro:
    #• Tipo de usuário:
    #• Total de dias:
    nome = input('Livro: ')
    tipo_usuario = input('Tipo de usuário: ').upper()
    print(f'Nome do livro: {nome}')
    print(f'Tipo de usuário: {tipo_usuario}')
    print(f'Total de dias: {10 if tipo_usuario == "PROFESSOR" else 3}')

    #22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
    #    informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
    #    12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.
    kms = int(input('kms percorridos: '))
    tipo_carro = input('Tipo do Carro: ').upper().strip()[0]
    consumo = 0.0
    if tipo_carro == 'A':
        consumo = kms / 12
    elif tipo_carro == 'B':
        consumo = kms / 9
    else:
        consumo = kms / 8
    print(f'Consumo: {round(consumo, 1)} litros')

    #23. Crie um programa que informe a quantidade total de calorias de uma refeição
    #    a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
    #    bebida conforme a tabela a seguir.
    #Prato                  Sobremesa               Bebida
    #Vegetariano 180cal     Abacaxi 75cal           Chá 20cal
    #Peixe 230cal           Sorvete diet 110cal     Suco de laranja 70cal
    #Frango 250cal          Mousse diet 170cal      Suco de melão 100cal
    #Carne 350cal           Mousse chocolate 200cal Refrigerante diet 65cal
    prato = input('Prato principal: ').strip().upper()
    bebida = input('Bebida: ').strip().upper()
    sobremesa = input('Sobremesa: ').strip().upper()    
    calorias = 0
    calorias += 180 if prato == 'VEGETARIANO' else 0
    calorias += 230 if prato == 'PEIXE' else 0
    calorias += 250 if prato == 'FRANGO' else 0
    calorias += 350 if prato == 'CARNE' else 0
    calorias += 20 if bebida == 'CHA' else 0
    calorias += 70 if bebida == 'SUCO DE LARANJA' else 0
    calorias += 100 if bebida == 'SUCO DE MELAO' else 0
    calorias += 65 if bebida == 'REFRIGERANTE DIET' else 0
    calorias += 75 if sobremesa == 'ABACAXI' else 0
    calorias += 110 if sobremesa == 'SORVETE DIET' else 0
    calorias += 170 if sobremesa == 'MOUSSE DIET' else 0
    calorias += 200 if sobremesa == 'MOUSSE DE CHOCOLATE' else 0
    print(f'Total de calorias: {calorias} cal')    

    #24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
    #    cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
    #    carro deve ser renovado é determinado pelo último número da placa do mesmo,
    #    faça um programa que, a partir da leitura da placa do carro, informe o mês
    #    em que o emplacamento deve ser renovado.
    placa = input('Placa: ')
    mes = int(placa[len(placa)-1])
    data = datetime(2022,mes,1)
    print(data.strftime('%b'))

    #25. A prefeitura contratou uma firma especializada para manter os níveis de
    #    poluição considerados ideais para um país do 1º mundo. As indústrias,
    #    maiores responsáveis pela poluição, foram classificadas em três grupos.
    #    Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
    #    aceitável é até 0,25, fazer um programa que possa imprimir intimações de
    #    acordo com o índice e a tabela a seguir:
    #Índice Indústrias que receberão intimação
    #0,3 1º grupo
    #0,4 1º e 2º grupos
    #0,5 1º, 2º e 3º grupos
    indice = float(input('Índice de Poluição: '))
    if indice >= 0.5:
        print('1º, 2º e 3º grupo')
    elif indice >= 0.4:
        print('1º e 2º grupo')
    elif indice >= 0.3:
        print('1º grupo')
    else:
        print('Não receberá intimação')

main()
