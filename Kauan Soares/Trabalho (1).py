while True:
  nome = input("Digite o seu nome! ")
  horas_trabalhadas = int(input("Digite aqui o número de horas do trabalho: "))
  salario_por_hora = int(input("Digite seu salário por hora: "))
  print(f"Nome:{nome}")
  print(f"Horas trabalhadas:{horas_trabalhadas}")
  print(f"Salário por hora:{salario_por_hora}")

  salario_bruto = horas_trabalhadas * salario_por_hora
  print(f"Salário bruto: R${salario_bruto}")

  if salario_bruto > 2000:
    bonus = salario_bruto * 0, 1
    salario_bruto_bonus = salario_bruto + bonus
    print(f"Salário bruto depois do bônus: R${salario_bruto_bonus}")
  else:
    print(f"Seu salário está muito baixo para o bônus")

  continuar = input("Deseja ver novamente? (s/n):")
  if not continuar.lower() == "s":
    print("Encerramento do sistema!")  
    break
