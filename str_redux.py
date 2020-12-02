#  Reese Allen  rga2uz  CS 1110-004  Apostolellis

def myfind(s,t):
    """
    :param s: the string we are looking for param t in
    :param t: what we are looking for
    :return: the position of the first character of t in s
    """
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i+j] != t[j]:
                break
            if j == len(t)-1:
                return i
    return -1


def mysplit(youngmoney):
    """
    :param youngmoney: the string being split
    :return: the split up string as a list
    """
    q = []
    y = ''
    for i in youngmoney:
        if i != ' ':
            y += i
        elif i == ' ':
            q.append(y)
            y = ''
    q.append(y)
    return q






