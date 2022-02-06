import jogos
def jogar():
    print(".")
    print(".* . * . * . * . * . *")
    print(".* . * (\ ***/) * . *")
    print(".* . * ( \(_)/ ) * . *")
    print(".* . * (_ /|\ _) * . *")
    print(".* . * . /___\ * . *")
    print("*. * . * . * . . * . *")
    print("\n\nBem-vindo ao jogo da forca!!!!!")

    arquivo = open("jogo","r")
    #agora o sistema vai escolher uma palavra secreta
    lista = []
    for palavra in arquivo:
        lista = lista + [palavra.strip()]


    i = 0
    for item in lista:
        i = i + 1
    #para o index i ficar dentro do range da lista
    i = i - 1

    import random

    palavra_secreta = lista[random.randrange(0,i)]

    arquivo.close()

    #contar letras
    contador = 0
    for leter in palavra_secreta:
        contador = contador + 1

    #Começar o jogo:


    palavra_secreta = palavra_secreta.upper()
    palavra_secreta = list(palavra_secreta)
    errou = False
    acertou = False
    palavra_completavel = []
    tentativas = 1
    total_tentativas = contador * 3
    print("\n\nVocê tem {} tentativas".format(total_tentativas))
    restante = total_tentativas


    for letra in palavra_secreta:
        palavra_completavel.append("_")

    while(not errou and not acertou):
        print(palavra_completavel)
        chute = input("\nDigite uma letra: ")
        chute = chute.upper().strip()
        if(chute in palavra_secreta):
            print("Boa!Você acertou")
            index = 0
            for caracter in palavra_secreta:
                if(caracter == chute):
                    palavra_completavel[index] = chute

                acertou = palavra_secreta == palavra_completavel
                if(acertou):
                    print("Parabéns!!! Você ganhou o jogo.\nA palavra secreta é {}".format(palavra_secreta))
                    break
                index = index + 1

        else:

            tentativas = tentativas + 1
            restante = restante - 1
            print("Lhe resta {} tentativas!".format(restante))
        errou = tentativas == total_tentativas
        if(errou):
            print("Infelizmente suas tentativas acabaram! A palavra secreta era {}".format(palavra_secreta))




if(__name__=="__main__"):
    jogar()




