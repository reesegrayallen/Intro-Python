# Reese Allen   rga2uz    CS 1110-004    Apostolellis


def check(n):
    """
    :param n: The credit card number we are checking to see if it is valid
    :return: Whether or not (true or false) the card number is valid
    """
    n = str(n)
    num_sum = 0
    double_sum = 0
    for i in range(-1, -(len(n)+1), -2):
        num_sum += int(n[i])
    new_string = ""
    for j in range(-2, -(len(n)+1), -2):
        new_string += n[j]
    newest_string = ""
    for g in new_string:
        newest_string += str(int(g)*2)
    for h in range(0, len(newest_string), 1):
        double_sum += int(newest_string[h])
    if (num_sum + double_sum) % 10 == 0:
        return True
    else:
        return False




