import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Chute uma letra ").strip().upper()
        if(chute in palavra_secreta):
            index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("Você tem {} tentativas até ser enforcado".format(6 - erros))



    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")



def imprime_mensagem_abertura():
    print("**********************************")
    print("****Bem vindo ao jogo de forca****")
    print("**********************************")
    return
def carrega_palavra_secreta():
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

if(__name__ == "__main__"):
    jogar()