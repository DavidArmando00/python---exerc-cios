n = int(input("Digite um número inteiro positivo: "))

soma = 0
for i in range(1, n + 1):
    soma += i

print("A soma de 1 até", n, "é:", soma)