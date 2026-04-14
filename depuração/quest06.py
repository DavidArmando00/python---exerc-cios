idade = int(input("Digite sua idade: "))
if idade <= 12:
   print("Criança")
if idade > 12 and idade <= 17:
   print("Adolescente")
if idade > 17 and idade <= 59:
   print("Adulto")
elif idade > 59:
   print("Idoso")
