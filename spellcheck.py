# Reese Allen  rga2uz   CS 1110  Apostolellis

import urllib.request

url = "http://cs1110.cs.virginia.edu/files/words.txt"

file = urllib.request.urlopen(url)

text_flag = True

word_list = []

for line in file:
    row = line.decode('utf-8').lower().strip()
    word_list.append(row)

print("Type text; enter a blank line to end.")
while text_flag:
    user_text = (input(""))
    misspelled = []
    if user_text:
        user_string = user_text.split()
        for element in user_string:
            element = element.strip(".?!,()'" + '"')
            if element.lower() not in word_list:
                misspelled.append(element)
        for word in misspelled:
            if word != "":
                print("  MISSPELLED:", word)

    if not user_text:
        text_flag = False


file.close()
