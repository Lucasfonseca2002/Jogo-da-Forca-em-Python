import random

def jogar_forca():
    palavras = [
        "python",
        "programacao",
        "desenvolvimento",
        "jogo",
        "computador",
        "algoritmo",
        "logica",
        "dados",
        "estrutura",
        "frutas",
        "legumes",
        "verduras",
        "carro",
        "moto",
        "bicicleta",
        "caminhao",
        "onibus",
        "avião",
        "barco",
        "navio",
        "trem",
        "trator",
        "Brasil",
        "Argentina",
        "Chile",
        "Estados Unidos",
    ]
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ["_"] * len(palavra_secreta)
    tentativas = 5
    letras_erradas = []

    while True:
        print("\n" + " ".join(letras_descobertas))
        print("Tentativas restantes: ", tentativas)
        print("Letras erradas: ", " ".join(letras_erradas))

        letra = input("Digite uma letra: ").lower()

        if letra in letras_erradas or letra in letras_descobertas:
            print("Você já tentou essa letra. Tente novamente!")

        elif letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_descobertas[i] = letra

            if "_" not in letras_descobertas:
                print("\nParabéns! Você venceu! A palavra era:", palavra_secreta)
                break

        else:
            letras_erradas.append(letra)
            tentativas -= 1

            if tentativas == 0:
                print("\nGame over! A palavra secreta era:", palavra_secreta)
                break


jogar_forca()
