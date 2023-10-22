"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 10/10 
Condicional - 5/5 
Saída de Resultados - 2,5/5 * o salário com bônus foi calculado mesmo quando menor que 2000 
Total: 27,5
"""

def repetir():   
    nome_funcionario = input("Digite o nome do funcionario: ")
    while True:
            try:
                horas_trabalhadas = float(input("Digite as horas trabalhadas: "))
                if horas_trabalhadas <= 0:
                    print("Isira valores maior que 0")
                else:
                    break
            except:
                print("Valor inserido é invalido!")
    while True:
            try:
                salario_hora = float(input("Digite o quanto ele recebe por hora: "))
                if salario_hora <= 0:
                    print("Isira valores maior que 0")
                else:
                    break
            except:
                print("Valor inserido é invalido!")

    salario_bruto = salario_hora * horas_trabalhadas
    bonus = salario_bruto *  0.10
    salario_bonus = salario_bruto + bonus

    print(f"Funcionario: {nome_funcionario}")
    print(F"Salario: {salario_bruto}")
    if salario_bruto >= 2000:
            print("Você recebeu um bonus de 10%!")
            print(f"Salario final R$ {salario_bonus}")
    else:
        print("Você não recebeu bônus este mês!")
        print(f"Saralrio final R$ {salario_bonus}")
repetir()
confirmacao = input("Quer pesquisar outro funcionario? sim/não ")
while True:
    try:
        if confirmacao == "sim":
                repetir()
        else:
             break
    except:
     print("Valor invalido! Tente usar sim ou não")
