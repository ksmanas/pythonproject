# player 1 and player 2 are playing
# rock : 1, scissors : 2, paper: 3
# Rock beats scissors = 1 - 2 = -1
# Scissors beats paper = 2 - 3 = -1
# Paper beats rock = 3 - 1 = 2
# player1 is [-1,2]
# Rock beats scissors = 2 - 1 = 1
# Scissors beats paper = 3 - 2 = 1
# Paper beats rock = 1 - 3 = -2
# player2 is [1,-2]
# announce the winner
# type quit to quit the game

name1 = str(input("Enter your name: "))
name2 = str(input("Enter your name: "))
player1Results = [0]
player2Results = [0]

while True:
    player1 = str(input("Enter rock, paper, or scissors: "))
    player2 = str(input("Enter rock, paper, or scissors: "))
    game = {"rock": 1, "scissors": 2, "paper": 3}
    a = game.get(player1)
    b = game.get(player2)
    diff = a - b

    if diff in [-1, 2]:
        print(name1 + " is the winner \n")
        player1Results.append(1)
        if str(input("Enter y to continue ")) == 'y':
            continue
        else:
            print("Game over")
            print(name1, sum(player1Results))
            print(name2, sum(player2Results))
            break
    elif diff in [1, -2]:
        print(name2 + " is the winner \n")
        player2Results.append(1)
        if str(input("Enter y to continue ")) == 'y':
            continue
        else:
            print("Game over")
            print(name1, sum(player1Results))
            print(name2, sum(player2Results))
            break
    else:
        print("Its a tie")










