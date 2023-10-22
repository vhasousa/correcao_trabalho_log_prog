"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 10/10 
Condicional - 5/5 
Saída de Resultados - 5/5
Total: 30 *
"""

while True:
      nome = input("Qual o nome do funcionário?")

      while True:
          try:
            hora_trabalhada = int(input("Número de horas trabalhadas no mês: "))
            if hora_trabalhada > 0:
                break
            else:
                print("O número de horas deve ser maior que zero.")  
          except:
            print("Por favor, digite um número valido.")

      while True:
          try:
            salario_hora = float(input("Qual o valor da hora trabalhada? "))
            if salario_hora > 0:
                break
            else:
                print("O valor da hora trabalhada deve ser maior que zero.")
          except:
              print("Por favor, digite um número valido.")

      salario_bruto1 = hora_trabalhada * salario_hora

      if salario_bruto1 > 2000:
          salario_bruto2 = (salario_bruto1 * 0.10) + salario_bruto1
          bonus = "Sim"
      else:
          salario_bruto2 = salario_bruto1
          bonus = "Nâo"

      print (f"\nNome do Funcionario: {nome}, Salario Bruto: R${salario_bruto1}, Teve bonus: {bonus}, Salario final: R${salario_bruto2}")

      resposta = input("\nDeseja calcular o bônus de outro funcionário? (S/N): ")
      if resposta.lower() != 's':
          break