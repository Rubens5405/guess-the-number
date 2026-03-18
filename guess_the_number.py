import random

opcao = random.randint(1, 51)
opcao = 10 
tentativas = 0
max_tentativas = 5

print("Encontre o número entre 1 e 50 (Você tem 5 tentativas).")

while max_tentativas > 0:
    try:
        tentativa = int(input(f"{tentativas + 1}ª tentativa:"))

        if tentativa == opcao:
            print(f"Você ganhou! A respota era: {opcao}.")
            break

        elif tentativa > opcao:
            print(f"O número é menor que {tentativa}.")

        elif tentativa < opcao:
            print(f"O número é maior que {tentativa}.")

        tentativas += 1
        max_tentativas -= 1

    except ValueError:
        print ("Valor inválido, tente novamente.")

if tentativa != opcao:
    print(f"Você perdeu! A resposta era: {opcao}.")
