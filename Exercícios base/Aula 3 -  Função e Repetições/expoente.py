# 1) Programar um pequeno sistema utilizando função. O usuário deve digitar o número base e o seu expoente. A função deve retornar o resultado da exponenciação.

numeroBase = float(input("Digite o número base: "))
numeroExpoente = float(input("Digite o expoente: "))


def exponenciacao(base=1, expoente=2):
    return base ** expoente 


print (exponenciacao(numeroBase, numeroExpoente))