# Reese Allen rga2uz   Apostolellis CS1110-004


def binop(s):
    if "*" in s:
        return int(s[0:s.find("*")]) * int(s[s.find("*")+1:len(s)])
    elif "+" in s:
        return int(s[0:s.find("+")]) + int(s[(s.find("+")+1):len(s)])
    elif "/" in s:
        return int(s[0:s.find("/")]) / int(s[s.find("/")+1:len(s)])
    elif "-" in s:
        return int(s[0:s.find("-")]) - int(s[s.find("-")+1:len(s)])


