"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 10/10 
Condicional - 5/5 
Saída de Resultados - 5/5
Total: 30
"""

nome_funcionario = input("Digite o nome do funcionário: ")

while True:
    try:
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
        if horas_trabalhadas >= 0:
            break
        else:
            print("Por favor, digite um valor não negativo.")
    except ValueError:
        print("Por favor, digite um número válido.")

while True:
    try:
        salario_por_hora = float(input("Digite o salário por hora: "))
        if salario_por_hora >= 0:
            break
        else:
            print("Por favor, digite um valor não negativo.")
    except ValueError:
        print("Por favor, digite um número válido.")

salario_total = horas_trabalhadas * salario_por_hora

print(f"Nome do funcionário: {nome_funcionario}")
print(f"Salário total no mês: R${salario_total:.2f}") 


salario_bruto = horas_trabalhadas * salario_por_hora

if salario_bruto > 2000:
    
    bonus = 0.10 * salario_bruto
    salario_bruto += bonus

print(f"Nome do funcionário: {nome_funcionario}")
print(f"Salário bruto no mês: R${salario_bruto:.2f}")



nome_funcionario = input("Digite o nome do funcionário: ")

while True:
    try:
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
        if horas_trabalhadas >= 0:
            break
        else:
            print("Por favor, digite um valor não negativo.")
    except ValueError:
        print("Por favor, digite um número válido.")

while True:
    try:
        salario_por_hora = float(input("Digite o salário por hora: "))
        if salario_por_hora >= 0:
            break
        else:
            print("Por favor, digite um valor não negativo.")
    except ValueError:
        print("Por favor, digite um número válido.")

salario_bruto = horas_trabalhadas * salario_por_hora

recebeu_bonus = False
if salario_bruto > 2000:
    
    bonus = 0.10 * salario_bruto
    salario_bruto += bonus
    recebeu_bonus = True

print(f"Nome do funcionário: {nome_funcionario}")
print(f"Salário bruto: R${salario_bruto:.2f}")
if recebeu_bonus:
    print("Recebeu bônus: Sim")
else:
    print("Recebeu bônus: Não")
print(f"Salário final: R${salario_bruto:.2f}")

































