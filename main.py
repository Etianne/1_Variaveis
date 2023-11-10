# declaração de variáveis
nome = "Etianne"
idade = 44
altura = 1.55
peso = 57

print("Olá, mundo!")

# imprimir na tela o valor das variáveis
print(nome) 
print(idade)
print(altura)
print(peso)

print("O meu nome é", nome, "e tenho", idade, "anos. E tenho,", altura, "m e peso", peso, "kg.")

print(type(nome)) 
print(type(idade))
print(type(altura))
print(type(peso))

aluno = input("Digite o nome do aluno: ")
print("O aluno é o", aluno)


# Execicio 1


Nome = input("Qual o seu nome: ")
print("Olá,", Nome, "! Seja bem-vindo ao mundo da programação em Python!")

print(type(Nome))



# Exercicio 2


seu_nome = input("Digite seu nome: ")
idade_amigo = input("Digite a idade do seu melhor amigo: ")

mensagem = "Olá, " + seu_nome + "! Seu melhor amigo tem " + idade_amigo + " anos de idade."

print(mensagem)