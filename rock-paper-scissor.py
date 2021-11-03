import random

comp_guess = random.choice(["Rock", "Paper", "Scissor"])
user_guess = input("Enter either Rock, paper or Scissor: ")

print("Computer guessed: ", comp_guess)

if(user_guess == comp_guess):
    print("It's a Tie!!")
elif(user_guess == "Rock"):
    if(comp_guess == "Scissor"):
        print("You win!")
    else:
        print("You Lose!")
elif(user_guess == "Paper"):
    if(comp_guess == "Rock"):
        print("You win!")
    else:
        print("You Lose!")
elif(user_guess == "Scissor"):
    if(comp_guess == "Paper"):
        print("You win!")
    else:
        print("You Lose!")
