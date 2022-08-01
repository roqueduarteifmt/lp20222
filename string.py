nome = "   João Paulo   "
print(len(nome))             #tamanho da string
nome = nome.strip()          #remove os espaços em branco nas extremidades
print(len(nome))
print(nome[1])               #o primeiro caractere é o de posição 0
print(nome[2:4])             #de 2 a 3 (último não incluso)
print(nome[-5:-1])           #começa a contagem pelo final da string
print(nome[0:10:2])          ##de 0 a 10 (último não incluso) saltando duas posições a cada caractere
print(nome.lower())          #transforma em minúsculo
print(nome.upper())          #transforma em maiúsculo
print(nome.replace("o","0")) #substitui a string
print(nome.split(" "))       #returns ["João","Paulo"]
print("au" in nome)          #retorna True se existe na string
print("au" not in nome)      #retorna True se não existe na string
idade = 40
texto = "Meu nome é {} e tenho {} anos."
print(texto.format(nome,idade))