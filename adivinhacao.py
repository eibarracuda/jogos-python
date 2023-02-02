def jogar():
    import random


    print("**********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("**********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha um nivel de dificuldade")
    print("(1) Fácil | (2) Médio | (3) Difícil")

    nivel = int(input("Digite o nivel"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite seu chute (1 a 100)"))
        print("Você digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Digite um numero válido")
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if (acertou):
            print("*********************************************")
            print("****** Você acertou e fez {} pontos! ******".format(pontos))
            print("*********************************************")
            break
        else:
            if(chute_maior):
                print("****  Você errou :( ****\nSeu chute foi MAIOR que o numero secreto")
            elif(chute_menor):
                print("**** Você errou :( ****\nSeu chute foi MENOR que o numero secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("Fim do jogo ...")
if(__name__ == "__main__"):
    jogar()