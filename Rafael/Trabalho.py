"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 10/10 
Condicional - 5/5 
Saída de Resultados - 2,5/5 *mesmo não recebendo bônus o salário deveria ser mostrado. Quando o salário é abaixo de 2000 a mensagem só retorna que ele não recebeu o bônus
Total: 27,5
"""

def reply():

    nome = input("Digite seu nome: ")
    h = int(input("Informe as horas trabalhadas no mes: "))
    salarioh = int(input("informe seu salario por hora: "))
    salarioBr = h * salarioh
    bonus = salarioBr / 10
    salarioB = salarioBr + bonus

    if salarioBr >= 2000:
        print(f"voce {nome} ganhou um bonus de 10% e seu salario e {salarioB} ")
    elif salarioBr < 2000:
        print(f"voce {nome} nao recebeu o bonus de 10%")
while True:
    resposta = input("Voce deseja ver o salario de um funcionario? 's' ou 'n'")
    if resposta.lower()  == 's':
    
        reply()
        print ("Carregando o codigo... ") 
    elif resposta.lower() == 'n' :
            break
        
    else:
        print("Opcao ivalida, por favor digite s ou n")