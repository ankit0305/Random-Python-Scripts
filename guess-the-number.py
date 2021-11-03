from random import randrange

value = randrange(6)
guess = input("Enter a number between 0-5: ")
if(int(guess) == value):
    print("You win 100!!")
else:
    print("You lose 100!! The number was ", value)
