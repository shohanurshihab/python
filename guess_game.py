import random
number = random.randint(1,10)
print("Welcome to the game : Guess the number \n Your name : ",end="")
name = input()
print("Hey",name,", try to guess the number I have in my mind! \n Your guess : ",end="")

for guesstaken in range(1,4):
    guess = int(input())
    if guess < number:
        print("Try a bit higher! -> ",end="")
    elif guess > number:
        print("Try a bit lower! -> ",end="")
    else:
        break
if number == guess:
    print("Congratulation! You guessed it right within ",guesstaken," guess")
else:
    print("Sorry mate! You couldn't hit it!")