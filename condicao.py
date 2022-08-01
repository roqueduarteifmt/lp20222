nota1 = float(input('Digite a nota do 1Bim: '))
nota2 = float(input('Digite a nota do 2Bim: '))
media = (nota1 + nota2)/2
if media >= 6:
    print(f'Aprovado com média {media}')
elif media >=3:
    pf = float(input('Digite a nota da Prova Final: '))
    media = (media + pf) / 2
    if media >= 5:
        print(f'Aprovado na Recuparação com média {media}')
    else:
        print(f'Reprovado na Recuperação com média {media}')
else:
    print(f'Reprovado com média {media}')