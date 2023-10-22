"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 10/10
Condicional - 5/5 
Saída de Resultados - 5/5
Total: 30 *
"""

while True:
  nome = input("Digite aqui seu nome:")
  horas_trabalhadas_mês = int(
      input("Digite aqui o número de horas trabalhadas:"))
  salario_hora = float(input("Digite aqui seu salário p/hora:"))
  print(f"Nome:{nome}")
  print(f"Horas trabalhadas:{horas_trabalhadas_mês}")
  print(f"Salário p/hora:{salario_hora}")

  salario_bruto = horas_trabalhadas_mês * salario_hora
  print(f"Salário bruto: R${salario_bruto}")

  if salario_bruto > 2000:
    bonus = salario_bruto * 0.1
    salario_bruto_com_bonus = salario_bruto + bonus
    print(f"Salário bruto após bônus: R${salario_bruto_com_bonus}")
  else:
    print(f"Seu salário está abaixo do mínimo para o bônus")

  continuar = input("Deseja consultar novamente ? (s/n):")
  if not continuar.lower() == "s":
    print("Encerramento do sistema!")
    break
