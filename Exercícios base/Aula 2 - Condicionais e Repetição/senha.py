#  Criar um programa que simule o login de um roteador. O nome de usuário (username) é "admin" e a senha (password) "123". Perdir ao usuário para digitar username e password. Caso os dados estejam corretos, mostrar uma mensagem "Login efetuado!", caso contrário "Login falhou!". (DESAFIO: Mostrar mensagens específicas para erro de username, de password ou de ambos).

username = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if username == 'admin' and senha == '123':
    print(f'Login efetuado!')
elif username == 'admin' and senha != '123':
    print(f'Login falhou! Senha incorreta.')
elif username != 'admin' and senha == '123':
    print(f'Login falhou! Nome de usuário incorreta.')
else:
    print(f'Login falhou! Usuário e senha incorretos!')