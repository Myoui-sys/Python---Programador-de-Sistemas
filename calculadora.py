n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Qual opção você quer? "))

if opcao == 1:
    print(n1 + n2)
elif opcao == 2:
    print(n1 - n2)
elif opcao == 3:
    print(n1 * n2)
elif opcao == 4:
    print(n1 / n2)
else: 
    print("Não existe esse número no Menu")