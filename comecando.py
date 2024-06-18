import random
import time
nome = ['pedra' , 'papel' , 'tesoura']


i = 0
limite = 3
while True:
        if i < limite :

            sorteio = random.choice(nome)
            print("Escolha uma das opçôes abaixo :\n\n|1-PEDRA|\n|2-PAPEL|\n|3-TESOURA|\n|0-SAIR| ")
            fale = str(input("\nFaça a sua escolha : "))
            ganhou = "\n $$$$ VOCÊ GANHOU $$$$\n"
            perda = f"\n|||!!!### VOCÊ PERDEU! ###!!!|||\n"
            empate = f"\n|||!!!### EMPATE ###!!!|||\n"

            match fale :
                case '1' :
                        if sorteio == 'pedra' :
                            print(empate)
                        elif sorteio == 'papel' :
                            print(perda)
                        elif sorteio == 'tesoura' :
                           print(ganhou)
                           i += 1

                case '2' :
                        if sorteio == 'pedra':
                            print(ganhou)
                            i += 1
                        elif sorteio == 'papel':
                            print(empate)
                        elif sorteio == 'tesoura':
                            print(perda)

                case '3' :
                        if sorteio == 'pedra':
                            print(perda)
                        elif sorteio == 'papel':
                            print(ganhou)
                            i += 1

                        elif sorteio == 'tesoura':
                            print(empate)

                case '0' :
                        break
                case _ :
                        print ("\n!!!! OPÇÃO INVÁLIDA !!!!\n\n******* TENTE NOVAMENTE *******")
            print(i)

        else :
            break
