# Em uma fábrica de reciclagem de materiais, cada 10kg de plástico rendem R$2,00 cada 30kg de papel rendem R$3,00 e cada 50kg de metal rendem R$5,00. Perguntar ao usuário a quantidade (kg) de cada material que deseja entregar na fábrica e mostrar o total que receberá em reais.
rendimentoPlastico = 2
rendimentoPapel = 3
rendimentoMetal = 5



plasticoEntregue = float(input("Quanto de plastico irá reciclar: "))
papelEntregue = float(input("Quanto quilos de papel irá reciclar: "))
metalEntregue = float(input("Quanto quilos de metal irá reciclar: "))

dinheiroPlastico =(plasticoEntregue / 10 )* rendimentoPlastico
dinheiroPapel =( papelEntregue / 30 )* rendimentoPapel
dinheiroMetal =(metalEntregue / 50 ) * rendimentoMetal 


total = dinheiroPlastico + dinheiroPapel + dinheiroMetal

print("Recebeu", dinheiroPlastico, "reais pela reciclagem do plástico.")
print("Recebeu", dinheiroPapel, "reais pela reciclagem do papel.")
print("Recebeu", dinheiroMetal, "reais pela reciclagem do metal.")
print("Total em reais recebido pela reciclagem: ", total)
