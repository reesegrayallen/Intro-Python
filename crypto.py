# Reese Allen  rga2uz   &     Omar Borai  onb3ra


# 2.1 Shift Cypher

def encrypt_chunk(text,key):
    """
    :param text: The string that will be encrypted
    :param key: The desired shift for each character in the string
    :return: Prints the encrypted text
    """
    alph="abcdefghijklmnopqrstuvwxyz"
    alphCap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key=key%26
    for c in text:
        if c in alphCap:
            v = int(alphCap.find(c) + key)
            if v > 26:
                print(alphCap[v - 26], end="")
            elif (v - key) == -1:
                print(" ", end="")
            else:
                print(alphCap[v], end="")
        else:
            v = int(alph.find(c) + key)
            if v > 26:
                print(alph[v - 26], end="")
            elif (v - key) == -1:
                print(" ", end="")
            else:
                print(alph[v], end="")
    print("")
encrypt_chunk("Hello",4)
def decrypt_chunk(text,key):
    """
    :param text: The string that will be decrypted
    :param key: The key used for encrypting
    :return: Prints the decrypted text
    """
    alph = "abcdefghijklmnopqrstuvwxyz"
    alphCap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key % 26
    for c in text:
        if c in alphCap:
            v = int(alphCap.find(c) - key)
            if (v + key) == -1:
                print(" ", end="")
            elif v < 0:
                print(alphCap[v + 26], end="")
            else:
                print(alphCap[v], end="")
        else:
            v = int(alph.find(c) - key)
            if (v + key) == -1:
                print(" ", end="")
            elif v<0:
                print(alph[v + 26], end="")
            else:
                print(alph[v], end="")
    print("")


# 2.4 Ubbi Dubbi

print()
def encrypt_ubbi(text):
    """
    :param text: the string that will be encrypted

    """
    text = text.lower()
    vowels_str = "aeiou"
    cipher = ""
    for letter in text:
        if letter in vowels_str:
            cipher += "ub"

        cipher += letter

    print("Encrypted:",cipher)
    decrypt_ubbi = ""
    index = 0

    while index < len(cipher):
        if cipher[index] == 'u' and cipher[index + 1] == 'b':
            decrypt_ubbi += cipher[index + 2]
            index += 3
        else:
            decrypt_ubbi += cipher[index]
            index += 1

    print("Unencrypted:", decrypt_ubbi)
    print("")

encrypt_ubbi("hello")
encrypt_ubbi("hangman")
encrypt_ubbi("while loop")
encrypt_ubbi("computer science")

