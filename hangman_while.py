# Reese Allen  rga2uz   Apostollelis  CS 1110   , lab partner: Omar Borai  onb3ra

phrase = input("Enter a phrase: ")
print("")
key = "_".join(phrase)
key += "_"
key = key.lower()

while "_" in key:
    letter = input("Guess a letter: ").lower()
    print("")
    key = key.replace(letter + "_", letter + letter)
    print("The word to guess:", key[1:len(key):2])
    print("")
print("You won! The word was:", phrase)