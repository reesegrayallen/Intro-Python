import random

number = random.randint(1,10)
tries = 1

uname = input("Hello, What is your username?")

print("Hello", uname + ".", )

question = input("Would you like to play a game? [Yes/No] ")
if question == "No":
    print ("oh...okay")

if question == "Yes":
    print("I'm thinking of a number between 1 & 10")
    guess = int(input("Take a fucking guess then homie:"))
    if guess > number:
        print("Guess lower fam...")
if guess < number:
    print("Guess higher bud..")
while guess != number:
    tries += 1
    guess = int(input("Try again: "))
    if guess < number:
        print("Guess higher")
if guess == number:
    print ("You are correct! You win finally! The number was", number
