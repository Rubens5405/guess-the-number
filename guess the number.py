import random

opcao = random.randint(1, 51)


tentativa = int(input("Encontre o número entre 1 e 50: "))

for i in range(4):
    if tentativa == opcao:
        print("Você ganhou!")
        break
            
    elif tentativa > opcao:
        tentativa = int(input(f"Número menor que {tentativa}: "))

    elif tentativa < opcao:
        tentativa = int(input(f"Número maior que {tentativa}: "))

if tentativa != opcao:
    print(f"Você perdeu! A resposta era: {opcao}.")




