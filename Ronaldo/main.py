"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 5/10 * calculo do bônus realizado incorretamente
Condicional - 5/5 
Saída de Resultados - 2,5/5 * poderia colocar a mensagem de bônus para aparecer somente quando ele realmente fosse receber (salario>2000).
Total: 22,5
"""

# trabalho do senai

nome = (input("qual o nome do funcionário?"))
while True:
  try:
    hora = int(input("Número de horas trabalhadas no mês:"))
    if hora <= 0:
      print("Número de horas inválidas")
    else:
      print(f"O funcionário {nome} trabalhou {hora} horas no mês.") 
      break
  except:
      print("valor inserido é inválido. tente somente numero inteiro")


while True:
  try:
    salario = int(input("Salário por hora:"))
    if salario <= 0:
      print("Salário por hora inválido")
    else:
      print(f"O salário do funcionário {nome} é de {salario} reais por hora.")
      break
  except:
      print("valor inserido é inválido. tente somente numero inteiro")



calculo1 = hora * salario
print(f"o funcionário {nome} tem um salário bruto de {calculo1}")

if calculo1 > 2000:
 print(f"o funcionário {nome} receberá um bônus de 10%")

else:
  print(f"o funcionário {nome} não recebera um bônus")


calculo1 = hora * salario  * 10
print(f"o salario do funcionario {nome} com bônus será de {calculo1}")
