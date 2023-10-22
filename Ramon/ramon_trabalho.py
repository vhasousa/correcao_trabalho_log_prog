"""
Variáveis e Entrada de Dados - 10/10
Cálculo de Salário - 10/10 
Condicional - 5/5 
Saída de Resultados - 5/5
Total: 30
"""

print("Calculadora de cálculo salarial")
confirmacao = "sim"
while True:
    try:
      if confirmacao == "sim":
        nome = input("Informe o nome do funcionário! ")
        bonus = ""
        while True:
          try:
              horas_t = float(input("Informe o número de horas trabalhadas! "))
              if horas_t >= 0:
                  break
              else: 
                  print("O valor inserido está incorreto! ")
          except:
              print("O valor inserido está incorreto!")
        while True:
          try:
            valor_h = float(input("Informe agora o valor da hora trabalhada! "))
            if valor_h >= 0:
                  break
            else: 
                  print("O valor inserido está incorreto! ")
          except:
              print("O valor inserido está incorreto!")
        
        vbonus = 0
        salario_final = 0
        
        def calculo_salario_bruto(a, b):
          return a * b
        
        salario_mes = calculo_salario_bruto(horas_t, valor_h)
        
        if salario_mes > 2000:
          bonus = "você alcançou a meta e vai receber uma bonificação! "
          vbonus = (salario_mes / 100) * 10
          salario_final = salario_mes + vbonus
          
                
        else:
          
          bonus = "voce não alcançou a meta, e não vai receber uma bonificação! "
          salario_final = salario_mes
      
        print(f"O salário do funcionário {nome}, esse mês foi de R${salario_mes} , porém {bonus} \n Sendo assim seu salario final esse mês é de R${salario_final}! ")
        #confirmacao = input("Quer continuar ")
  
      elif confirmacao == "não":
        break
      else:  print("Digite \'sim\' ou \'não\'!  ")
    except:  
      print("O valor inserido está incorreto!")
      
    confirmacao = input("Quer fazer outra verificação? ")
print("Verificação encerrada!")    
  