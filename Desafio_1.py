# Faça um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
# Exemplo de Resultado: O Seu salário atual é de R$1500,00 com o aumento de 15% seu novo salário será de R$1725,00

salario = int(input("digite o seu salario  "))
novo_salario = (salario * 15)
porcentagem = (salario /100)
valor = (porcentagem + salario)

resultado = print (f"Sua porcentagm de aumento = {porcentagem} ,Então seu salario atual é de : {valor}")