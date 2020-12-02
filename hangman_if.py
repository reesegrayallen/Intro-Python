# Reese Allen  rga2uz   Apostollelis  CS 1110   , lab partner: Omar Borai  onb3ra



def hangman():
    phrase = input("Enter a phrase: ")
    print("")
    key = "_".join(phrase)
    key+="_"
    key=key.lower()

    letter=input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_",letter + letter) == key:
        print("")
    else:
        key=key.replace(letter + "_", letter + letter)
        print("The word to guess:" , key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")

    letter = input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_", letter + letter) == key:
        print("")
    else:
        key = key.replace(letter + "_", letter + letter)
        print("The word to guess:", key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")

    letter = input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_", letter + letter) == key:
        print("")
    else:
        key = key.replace(letter + "_", letter + letter)
        print("The word to guess:", key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")

    letter = input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_", letter + letter) == key:
        print("")
    else:
        key = key.replace(letter + "_", letter + letter)
        print("The word to guess:", key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")

    letter = input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_", letter + letter) == key:
        print("")
    else:
        key = key.replace(letter + "_", letter + letter)
        print("The word to guess:", key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")

    letter = input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_", letter + letter) == key:
        print("")
    else:
        key = key.replace(letter + "_", letter + letter)
        print("The word to guess:", key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")

    letter = input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_", letter + letter) == key:
        print("")
    else:
        key = key.replace(letter + "_", letter + letter)
        print("The word to guess:", key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")

    letter = input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_", letter + letter) == key:
        print("")
    else:
        key = key.replace(letter + "_", letter + letter)
        print("The word to guess:", key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")

    letter = input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_", letter + letter) == key:
        print("")
    else:
        key = key.replace(letter + "_", letter + letter)
        print("The word to guess:", key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")

    letter = input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_", letter + letter) == key:
        print("")
    else:
        key = key.replace(letter + "_", letter + letter)
        print("The word to guess:", key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")

    letter = input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_", letter + letter) == key:
        print("")
    else:
        key = key.replace(letter + "_", letter + letter)
        print("The word to guess:", key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")

    letter = input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_", letter + letter) == key:
        print("")
    else:
        key = key.replace(letter + "_", letter + letter)
        print("The word to guess:", key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")

    letter = input("Guess a letter: ").lower()
    print("")
    if key.replace(letter + "_", letter + letter) == key:
        print("")
    else:
        key = key.replace(letter + "_", letter + letter)
        print("The word to guess:", key[1:len(key):2])
        if "_" not in key:
            print("")
            print("You won, the word is:", phrase)
            return
        else:
            print("")



hangman()