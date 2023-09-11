
#  Crie um programa que solicite a senha de um usuário e depois, peça pra digitar novamente até que as duas senhas sejam correspondentes.
senha = 'seila'
senhaUser = input("Digite a senha: ")

while senhaUser != senha:
    senhaUser = input("Senha Incorreta. Digite a senha novamente :")
else:
    print("Senha correta. Login efetuado")