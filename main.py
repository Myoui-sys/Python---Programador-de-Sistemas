# # #E-commerce com atualização de estoque

# # estoque_inicial = 250

# # venda = 78

# # estoque_atualizado = 100

# # estoque_atual = (estoque_inicial - venda) + estoque_atualizado

# # print("O estoque atual é: ", estoque_atual)

# # # Armazenar variáveis

# # nome = "Ewerton Henrique"

# # idade = 23

# # altura = 1.75

# # print("Nome:", nome,"Idade:", idade,"Altura:", altura)

# # # Solicitação de dois números para somar, multiplicar, subtrair e dividir

# # numero_1 = int(input("Digite um número: "))
# # numero_2 = int(input("Digite outro número: "))

# # soma = numero_1 + numero_2
# # subtracao = numero_1 - numero_2
# # divisao = numero_1 / numero_2
# # multiplicacao = numero_1 * numero_2

# # print("A soma é: ", soma)
# # print("A subtração é: ", subtracao)
# # print("A divisao é: ", divisao)
# # print("A multiplicação é: ", multiplicacao)

# # # Solicitar nome do usuário para mensagem de boas-vindas

# # nome_usuario = str(input("Digite seu nome: "))
# # print("Boas vindas, ", nome_usuario)

# # # Nome na tela

# # meu_nome = "Dacy"
# # print("Oi! Meu nome é", meu_nome)

# # # Área de retângulo

# # largura = int(input("Digite a largura: "))
# # altura = int(input("Digite a altura: "))

# # area = largura * altura

# # print("A área do retângulo é:", area)

# # # Estrutura condicional

# # nome = str(input("Qual é o seu nome? "))

# # nota_1 = float(input("Digite a primeira nota: "))
# # nota_2 = float(input("Digite a segunda nota: "))
# # nota_3 = float(input("Digite a terceira nota: "))
# # nota_4 = float(input("Digite a quarta nota: "))

# # min_aprovacao = 7

# # media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
# # print("A sua média foi:", media)

# # if media >= min_aprovacao:
# #     print("Aprovado")
# # else: 
# #     print("Reprovado")

# # # Maior de idade ou menor de idade

# # nome_2 = str(input("Digite seu nome: "))
# # idade = int(input("Digite sua idade: "))

# # maioridade = 18
# # print("Seu nome é:", nome, "\nE você tem:", idade, "anos.")
# # if idade >= maioridade:
# #     print("Você é maior de idade!")
# # else:
# #     print("Você é menor de idade!")


# # # Positivo ou negativo

# # numero = int(input("Digite um número: "))

# # print("Você digitou o número:", numero)
# # if numero >= 0:
# #     print("Ele é positivo")
# # else: 
# #     print("Ele é negativo")

# # # Criar uma função com dois números para ver qual é maior que o outro

# # numero_1 = int(input("Digite um número: "))
# # numero_2 = int(input("Digite outro número: "))

# # if numero_1 > numero_2:
# #     print(numero_1, "é maior que", numero_2)
# # else:
# #     print(numero_2, "é maior que", numero_1)

# # # Número par ou ímpar

# # descobrir_numero = int(input("Digite um número para descobrir se é par ou ímpar: "))

# # if descobrir_numero % 2 == 0:
# #     print("Esse número é par: ", descobrir_numero)
# # else: 
# #     print("Esse número é ímpar: ", descobrir_numero)

# # # Uso de elif
# # media_nova = float(input("Digite a média: "))

# # if media_nova >= 7:
# #     print("Aprovado")
# # elif media_nova >= 4:
# #     print("Recuperação")
# # else:
# #     print("Reprovado")

# # # Três valores para saber qual é o maior e exibir média aritmetica ao final com resultado, informar qual é o menor e o maior valor entre os três
# # value_1 = float(input("Type one number: "))
# # value_2 = float(input("Type another number: "))
# # value_3 = float(input("Type the last number: "))

# # value_max = max(value_1, value_2, value_3)
# # value_min = min(value_1, value_2, value_3)

# # print("The max value is: ", value_max)
# # print("The min value is: ", value_min)


# # media_nova_1 = (value_1 + value_2 + value_3) / 3
# # print("The result is: ", media_nova_1)

# # # Verificar senha 

# # entrada_senha = str(input("Digite a senha: "))

# # if entrada_senha == "1234":
# #     print("Acesso permitido")
# # else:
# #     print("Acesso negado")

# # # Categoria de idade

# # age = int(input("Type your age: "))

# # if age < 12:
# #     print("Kid")
# # elif age < 18:
# #     print("Teenage")
# # else:
# #     print("Adult")



# # # Desconto

# # valor = int(input("Digite o valor: "))

# # if valor >= 5000:
# #     desconto = valor * 0.20
# # else:
# #     desconto = valor * 0.15

# # valor_final = valor - desconto

# # print("Seu desconto foi de: R$ ", desconto)
# # print("Seu valor a pagar é: R$ ", valor_final)

# # # Classificação com idade

# # idade_nadador = int(input("Digite sua idade: "))

# # print("Você digitou: ", idade_nadador)
# # if idade_nadador > 0 and idade_nadador <= 7:
# #     print("Infantil A")
# # elif idade_nadador > 7 and idade_nadador <= 10:
# #     print("Infantil B")
# # elif idade_nadador > 10 and idade_nadador <= 13:
# #     print("Juvenil A")
# # elif idade_nadador > 13 and idade_nadador <= 17:
# #     print("Juvenil B")
# # elif idade_nadador > 17 and idade_nadador <= 60:
# #     print("Adulto")
# # elif idade_nadador > 60: 
# #     print("Senior")
# # else:
# #     print("Idade náo existente")

# produto = str(input("Digite o produto: "))
# cor = str(input("Digite a cor: "))

# produto_1 = "caneta"
# cor_1 = "azul"

# if produto.lower() == produto_1 and cor.lower() == cor_1:
#     print("Verdadeiro")
# else: 
#     print("Falso")

# produto = str(input("Digite o nome do produto: "))
# cor = str(input("Digite a cor: "))

# produto_1 = "caneta"
# cor_1 = "azul"

# if produto.lower() == produto_1 or cor.lower() == cor_1:
#     print("Verdadeiro")
# else: 
#     print("Falso")

# Triângulo se cada lado for menor que a soma dos outros dois

# a = int(input("Digite o número do lado 1: "))
# b = int(input("Digite o número do lado 2: "))
# c = int (input("Digite o número do lado 3: "))

# if (b + c > a + b) and (b + c > a + c):
#     print(a, "é o menor lado")
# elif (a + c > a + b) and (a + c > b + c):
#     print(b, "é o menor lado")
# else:
#     print(c, "é o menor lado")