#Stored High Score
highScore = 1200

cont = True

while cont:
    #Player Score
    score = input("Enter your score: ")
    score = int(score)

    if score > highScore:
        print("Congratulations on your new HIGH SCORE!!! " + str(score))
        highScore = score
        response = input("Play Again? (y/n)\n>> ")
        if response == "y":
            cont = True
        else:
            cont = False
    else:
        print("Nice Try! HIGH SCORE: " + str(highScore))
        response = input("Play Again? (y/n)\n>> ")
        if response == "y":
            cont = True
        else:
            cont = False

print("Thanks for Playing!")