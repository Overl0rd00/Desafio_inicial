import random
import time
name = ['pedra' , 'papel' , 'tesoura']

def start () :
        i = 0
        limit = 3
        while True:
                if i < limit :

                    sweepstakes = random.choice(name)
                    print("Escolha uma das opçôes abaixo :\n\n|1-PEDRA|\n|2-PAPEL|\n|3-TESOURA|\n|0-SAIR| ")
                    speak = str(input("\nFaça a sua escolha : "))
                    wins = "\n $$$$ VOCÊ GANHOU $$$$\n"
                    loss = f"\n|||!!!### VOCÊ PERDEU! ###!!!|||\n"
                    draw = f"\n|||!!!### EMPATE ###!!!|||\n"

                    match speak :
                        case '1' :
                                if sweepstakes == 'pedra' :
                                    print(draw)
                                elif sweepstakes == 'papel' :
                                    print(loss)
                                elif sweepstakes == 'tesoura' :
                                 print(wins)
                                i += 1

                        case '2' :
                                if sweepstakes == 'pedra':
                                    print(wins)
                                    i += 1
                                elif sweepstakes == 'papel':
                                    print(draw)
                                elif sweepstakes == 'tesoura':
                                    print(loss)

                        case '3' :
                                if sweepstakes == 'pedra':
                                    print(loss)
                                elif sweepstakes == 'papel':
                                    print(wins)
                                    i += 1

                                elif sweepstakes == 'tesoura':
                                    print(draw)

                        case '0' :
                                break
                        case _ :
                                print ("\n!!!! OPÇÃO INVÁLIDA !!!!\n\n******* TENTE NOVAMENTE *******")
                    print(i)

                else :
                    break
start()
