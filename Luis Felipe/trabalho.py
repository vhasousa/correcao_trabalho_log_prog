"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 10/10 
Condicional - 5/5 
Saída de Resultados - 2,5/5 * faltou mostrar o salário já com o bônus no final
Total: 27,5
"""

nome_funcionario = input("Digite o nome do funcionário: ")
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_por_hora = float(input("Digite o salário por hora: "))

# Parte 2: Cálculo de Salário Bruto
salario_bruto = horas_trabalhadas * salario_por_hora

# Parte 3: Condicional para Bônus
if salario_bruto > 2000:
    bonus = 0.10 * salario_bruto
    salario_bruto += bonus
else:
    bonus = 0

# Parte 4: Saída de Resultados
print("\nNome do funcionário:", nome_funcionario)
print("Salário bruto:", salario_bruto)
if bonus > 0:
    print("Bônus de 10% aplicado: R$", bonus)