"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 10/10 
Condicional - 5/5 
Saída de Resultados - 2,5/5 * faltou mostrar o salário já com o bônus no final
Total: 27,5 *
"""

while True:
    funcionario = input("Nome do funcionário:" )

    while True:
        try:
            horas = float(input("Horas trabalhadas no mês: "))
            if horas < 0:
                print("Valor Inválido. Utilize números positivos." )
            else:
                break
        except:
                print("Valor Inválido. Utilize números inteiros.")

    while True:
        try:

            salarioh = float(input("Salário por hora: R$ "))
            if salarioh <= 0.01:
                print("Funcionarios recebem no minimo R$0.01" )
            else:
                break
        except:
             print("Valor Inválido. Utilize números inteiros.")

    calculo = horas * salarioh
    
    print(f"Nome do funcionario: {funcionario} ")
    print(f"Salario bruto: {calculo} ")

    if calculo > 2000:
     print(f"Recebeu o bônus.")

    elif calculo < 2000:
        print("Não recebeu o bônus.")

    if calculo > 2000:
     print(f"Salario final: R${calculo * 0.10} ")

    elif calculo < 2000:
       print(f"Salario final: R${calculo} ")

    resposta = input("\nDeseja calcular o bônus de outro funcionário? (S/N): ")
    if resposta.lower() != 's':
        break