# This is the complete code for the Project The Perfect Guess
import random

print("Welcome!")
a=random.randint(1,100)
b=None
guesses=0
while(b!=a):
    print("Guess the number by computer: ")
    b=int(input())
    guesses +=1
    if(b>a):
        print("The number is too Big,Enter Smaller Number. ")
    elif(b<a):
        print("The number is too small. Enter Bigger number. ") 
    else:
        print("The Guess is Correct ")

print(f"You guessed the correct number in {guesses} times! ")

with open("hiscore.txt","r") as f:
    Hiscore=int(f.read())

if(guesses<Hiscore):
    print("You have just broken the high score! ")
    with open('hiscore.txt',"w") as f:
        f.write(str(guesses))