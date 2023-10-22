"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 10/10 
Condicional - 5/5 
Saída de Resultados - 5/5
Total: 30*
"""

def calcular_salario():
  nome = input("Digite seu nome: ")
  while True:
      try:
          horas = float(input("Digite as horas trabalhadas mensalmente: "))
          if horas < 0:
              print("Horas não podem ser negativas. Tente novamente.")
          else:
              break
      except ValueError:
          print("Entrada inválida. Tente novamente.")

  while True:
      try:
          salario = float(input("Digite seu salário por hora: "))
          if salario < 0:
              print("Salário por hora não pode ser negativo. Tente novamente.")
          else:
              break
      except ValueError:
          print("Entrada inválida. Tente novamente.")

  calculo = horas * salario
  calculo_bonus = (10 * calculo) / 100
  bonus = calculo + calculo_bonus

  print(f"Nome do contratado: {nome}")
  print(f"Seu salário bruto é: R${calculo:.2f}")

  if calculo > 0 and calculo < 2000:
      print("Você não tem direito ao bônus.")
      print(f"Salário final: R${calculo:.2f}")
  else:
      print("Você tem direito ao bônus.")
      print(f"Salário final: R${bonus:.2f}")

while True:
  calcular_salario()
  resposta = input("Deseja calcular o bônus para outro funcionário? (s/n): ")
  if resposta.lower() != "s":
      print("Programa encerrado.")
      break
