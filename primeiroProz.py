quantidadeDePessoas = int(input("Quantidade de pessoas: "))
veiculoQuantidadeDeRoda = int(input("Quantas rodas o seu veiculo tem: "))
peso = int(input("Qual o peso: "))

if(veiculoQuantidadeDeRoda >= 4) and (peso > 6000):
  print("E")
elif(veiculoQuantidadeDeRoda >= 4) and (quantidadeDePessoas > 8):
  print("D")
elif(veiculoQuantidadeDeRoda >= 4) and (peso >= 3500 or peso <= 6000):
  print("C")
elif(veiculoQuantidadeDeRoda == 4) and (peso >= 3500 and quantidadeDePessoas <= 8):
  print("B")
else :
 print("A")