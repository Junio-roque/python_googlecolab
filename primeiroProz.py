quantidadeDePessoas = int(input("Quantidade de pessoas: "))
veiculoQuantidadeDeRoda = int(input("Quantas rodas o seu veiculo tem: "))
peso = int(input("Qual o peso: "))

if(veiculoQuantidadeDeRoda >= 4) and (peso > 6000):
  print("Veiculo de quatro roda e com peso mais de 6000kg.")
elif(veiculoQuantidadeDeRoda >= 4) and (quantidadeDePessoas > 8):
  print("Veiculo de quatro ou mais rodas que acomoda mais de oito pessoas.")
elif(veiculoQuantidadeDeRoda >= 4) and (peso >= 3500 or peso <= 6000):
  print("Veiculo com quatro rodas ou mais com peso entre 3500kg a 6000kg")
elif(veiculoQuantidadeDeRoda == 4) and (peso >= 3500 and quantidadeDePessoas <= 8):
  print("Veiculo com quatro rodas que pode acomodar ate oito pessoas de 3500kg")
else :
 print("Veiulo com duas ou três rodas.")