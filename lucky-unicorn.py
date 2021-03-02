import random

PRIZES = [["Unicorn", "4"], ["Donkey", "0"], ["Zebra", "0.5"], ["Horse", "0.5"]]


def statement_generator(text, symbol):
    length = len(text)+6
    print(symbol*length)
    print(symbol*2 + " "*(len(text)+2) + symbol*2)
    print(symbol*2 + " " + text + " " + symbol*2)
    print(symbol*2 + " "*(len(text)+2) + symbol*2)
    print(symbol*length)


def start_game():
    statement_generator("Welcome to Lucky Unicorn", "*")
    playingRounds = int(input("How much do you want to play with? "))
    played_before = input("Have you played the game before? [y]/[n]: ")
    if played_before == "n":
        print("You start by pressing <enter>. You will get either a horse, a zebra, a donkey or a unicorn.")
        print("\nIt costs $1 per round. Depending on your prize you might win some money back")
        print("\nUnicorn: +4 dollars\nHorse: -0.50 cents\nZebra: -0.50 cents\nDonkey: -1 dollar\n")
        print("To quit type 'xxx' instead of pressing enter\n")
    totalMoney = float(10)
    while True:
        gameInput = input("Press <enter> to start: ")
        while gameInput != "":
            if gameInput == "xxx":
                print("You have exited the game.\nYour balance is: ${}".format(str(totalMoney)))
                return
            gameInput = input("Press <enter> to start: ")
        while totalMoney > 0 and playingRounds > 0:
            prize = random.choice(PRIZES)
            playingRounds -= 1
            totalMoney += float(prize[1])-1
            statement_generator("You have won a "+str(prize[0])+". Your balance is now "+str(totalMoney), "=")
            gameInput = input("Press <enter> to continue or type 'xxx' to quit")
            while gameInput != "":
                if gameInput == "xxx":
                    print("You have exited the game.\nYour balance is: ${}".format(str(totalMoney)))
                    return
                gameInput = input("Press <enter> to continue or type 'xxx' to quit: ")
            if totalMoney == 0:
                print("You have run out of money! Thanks for playing!")
                return
            if playingRounds == 0:
                print("You have run out of money!\nYour balance is: ${}".format(str(totalMoney)))
                gameInput = input("Do you want to play again [y]/[n]: ")
                if gameInput == "n":
                    print("You have exited the game.\nYour balance is: ${}".format(str(totalMoney)))
                    return
    

start_game()
