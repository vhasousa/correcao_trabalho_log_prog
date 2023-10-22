"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 5/10 * calculo do bônus realizado incorretamente
Condicional - 5/5 
Saída de Resultados - 2,5/5 * mensagens de saída, principalmente na linha 36 ficou confusa.
Total: 22,5
"""

nome = input("Informe o nome do funcionario: ")

while True:
    try:
        hora_trabalhatas = float(input("Informe a hora de trablho do funcionario: "))
        break
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        salario_hora = float(input("Informe a hora salarial do funcionario: "))
        break
    except:
        print("Valor inserido está incorreto")

salario_bruto = (salario_hora * hora_trabalhatas) 


bonus= (salario_hora % salario_bruto) * 10

com_ou_sem_bonos= bonus + salario_bruto

if salario_bruto >=  2000 :
    print(f'O funcionario {nome}, com o salario de {salario_bruto},recebeu o seu salario mais a bunificação de {bonus}, salario final com bonos {com_ou_sem_bonos} ')
else:
   salario_bruto <= 1999
   print(f'O funcionario {nome}, com o salario de {salario_bruto},não recebeu a bunificação de 10% sem bonos {salario_bruto}') 