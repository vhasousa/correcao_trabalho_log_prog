"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 5/10 * na linha 27, no momento de calcular o bônus utilizou virgula ao invés de ponto. 
Condicional - 5/5 
Saída de Resultados - 2,5/5 *apresentou uma mensagem de erro
Total: 22,5

Ao final da execução o código apresentou o seguinte erro
Traceback (most recent call last):
  File "d:\Documentos\SENAI\Programador Back-End\Lógica de Programação\Prática\Aula 17 a 20 - Trabalho\Entregas\Kauan Soares\Trabalho.py", line 22, in <module>
    salario_bruto_bonus = salario_bruto + bonus
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
"""

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
    print("Seu salário está muito baixo para o bônus")

  continuar = input("Deseja ver novamente? (s/n):")
  if continuar.lower() != "s":
    print("Encerramento do sistema!")  
    break