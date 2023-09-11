# Uma cidade pretende apurar os votos de sua eleição. Faça um programa para ler o número total de eleitores. Em seguida o número de votos do candidato X, o número de votos do candidato Y, total de votos brancos e total de votos nulos (a soma desses quatro, deve ser igual ao total de eleitores). Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.


# somaVotos = int(input("Número total de eleitores: "))

votosCandidatoX = int(input("Digite o número de votos no candidato X:"))
votosCandidatoY = int(input("Digite o número de votos no candidato Y:"))
votosBrancos = int(input("Digite o número de votos em branco:"))
votosNulos = int(input("Digite o número de votos nulos:"))

somaVotos = votosCandidatoX + votosCandidatoY + votosBrancos + votosNulos


perCandidatoX = (votosCandidatoX * 100) / somaVotos
perCandidatoY = (votosCandidatoY * 100) / somaVotos
perBrancos = (votosBrancos * 100) / somaVotos
perNulos = (votosNulos * 100) / somaVotos

print("Número total de eleitores", somaVotos)
print("O percentual do candidato X é", perCandidatoX, "%")
print("O percentual do candidato Y é", perCandidatoY, "%")
print("O percentual de votos em brancos é", perBrancos,"%")
print("O percentual de votos nulos é", perNulos,"%")
