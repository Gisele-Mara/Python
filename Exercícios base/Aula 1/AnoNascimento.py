# Desenvolva uma programação que peça ao usuário para digitar o ano do seu nascimento no formato (YYYY) e o ano atual também no formato (YYYY). Em seguida mostre na tela qual a idade do usuário em anos, em meses, em dias e em semanas.

anoNascimento = int(input("Digite o ano de seu nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

idadeAnos =  anoAtual - anoNascimento

idadeMeses = idadeAnos * 12
idadeSemanas = idadeAnos * 52
idadeDias = idadeAnos * 365

texto = '''A idade do usuário em anos é  {}
em meses é {}, em semanas é {} e em dias {}'''
print(texto.format(idadeAnos, idadeMeses, idadeSemanas, idadeDias))