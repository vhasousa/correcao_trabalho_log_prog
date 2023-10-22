"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 10/10
Condicional - 5/5 
Saída de Resultados - 5/5
Total: 30 *
"""

from os import system
from keyboard import is_pressed
while is_pressed("ctrl") == False:
    system("cls")
    while is_pressed("ctrl") == False:
        
        try:
            nome_funcionario = str(input("Nome do Funcionario: "))
            horas_trabalhadas = int(input("Número de horas trabalhadas no mês: ")) 
            salario_hora = int(input("Salário por hora: "))
            break 
        except:
            print("Insira corretamente os valores!")
    
    calculo_salario_bruto = horas_trabalhadas * salario_hora
    bonus = False
    if calculo_salario_bruto > 2000:
        bonus = True
        calculo_salario_bonus = (calculo_salario_bruto / 100) * 110
    if bonus == True:
        print(f"Funcionario {nome_funcionario} com salario bruto de {calculo_salario_bruto}, Recebeu o bônus, {calculo_salario_bonus}")
    elif bonus == False:
        print(f"Funcionario {nome_funcionario} com salario bruto de {calculo_salario_bruto}, Não recebeu o bônus, {calculo_salario_bruto}")
    else:
        print("Ocorreu um erro!")
        break
    again = input("Deseja calcular o bônus de outro funcionario?(s/n)")
    if again == "n":
        break
        
