# Reese Allen  rga2uz   Apostollelis  CS 1110   , lab partner: Omar Borai  onb3ra

phrase = input("Enter a phrase: ")
print("")
print("Time to play hangman, you have 10 guesses!")
print("")
key = "_".join(phrase)
key += "_"
key = key.lower()
run = 0

while "_" in key:
    letter = input("Guess a letter: ").lower()
    print("")
    run += 1
    key = key.replace(letter + "_", letter + letter)
    print("The word to guess:", key[1:len(key):2])
    print("")
    # if letter*2 in key:
    #     print("You already guessed that letter")
    # if run == 10:
    #     print = "You lost, the word was "
print("You won! The word was:", phrase)