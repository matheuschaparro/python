import random
def jogar():

    estrelas="********************************"

    print(estrelas)
    print("Bem vindo ao jogo de advinhação!")
    print(estrelas)

    nivel=input("Qual o nível do jogo?\n(1)Fácil\n(2)Médio\n(3)Difícil\nDigite aqui: ")
    nivel=int(nivel)

    if(nivel==1):
        total_tentativas=5
    elif(nivel==2):
        total_tentativas=4
    elif(nivel==3):
        total_tentativas=3


    numero_secreto = round(random.uniform(1,100))

    rodada=1

    while(rodada<=total_tentativas):


        chute = input("Digite um número entre 1 e 100: ")
        chute=int(chute)





        print("Tentativa {} de {}".format(rodada,total_tentativas))

        igual=numero_secreto==chute
        maior=chute>numero_secreto
        menor=chute<numero_secreto


        if (igual):
            print("Parabéns!!! Você acertou")
            break

        else:
            if(maior):
                print("Você errou!!!Seu chute foi maior que o número secreto!\n")
            elif(menor):
                print("Você errou!!!Seu chute foi menor que o numero secreto\n")
            rodada = rodada + 1

    print("Fim de jogo!!!")

if(__name__=="__main__"):
    jogar()