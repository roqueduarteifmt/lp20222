#Recebendo como entrada o valor de um produto e o
#tipo de cliente (platinum, gold, bronze) calcular o
#desconto e apresentar ao final, o valor do produto,
#o valor do desconto e o valor final do produto com desconto
#Platinum 10%, gold 7%, bronze 4%

valorProduto = float(input("Informe o preço: "))
valorDesconto = 0
tipoCliente = input("Tipo do cliente: ").strip().upper()

if tipoCliente == 'PLATINUM':
    valorDesconto = valorProduto * 0.1
elif tipoCliente == 'GOLD':
    valorDesconto = valorProduto * 0.07
elif tipoCliente == 'BRONZE':
    valorDesconto = valorProduto * 0.04
else:
    valorDesconto = 0

print(f'Valor do Produto: R$ {valorProduto}\n')
print(f'Valor do Desconto: R$ {valorDesconto} ({tipoCliente})\n')
print(f'Valor a Pagar: R$ {valorProduto - valorDesconto}\n')



