"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 10/10
Condicional - 5/5
Saída de Resultados - 5/5
Total: 30*
"""

while True:

    nome = input("Digite o nome do funcionário: ")
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
    salario_hora = float(input("Digite o salário por hora: "))

    salario_bruto = horas_trabalhadas * salario_hora

    if salario_bruto > 2000:
        bonus = salario_bruto * 0.1
        salario_final = salario_bruto + bonus
        recebeu_bonus = "Sim"
    else:
        bonus = 0
        salario_final = salario_bruto
        recebeu_bonus = "Não"

    
    print("\nNome do funcionário:", nome)
    print("Salário bruto:", salario_bruto)
    print("Recebeu o bônus?:", recebeu_bonus)
    print("Salário final:", salario_final)

    
    opcao = input("\nDeseja calcular o bônus para outro funcionário? (sim/não): ")
    if opcao.lower() == "não":
        break