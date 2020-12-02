# Reese Allen   rga2uz   CS 1110-004   Apostolellis


def mymap(func, first):
    """
    :param func: the function given when mymap is called to be applied to every element in the first list
    :param first: the list provided when function is called that we are trying to alter
    :return: list containing the result of applying func to each element in the first list

    """
    new_list = []
    for i in first:
        new_list.append(func(i))

    return new_list



def myreduce(func, first):
    """

    :param func: the function to be used repeatedly on all elements of the list
    :param first: the list provided, the elements of which we will be using the function on and combining
    :return: result of using function repeatedly to combine all elements of the list into a single value
    """
    new_list = [] + first
    x = 0
    while x < (len(new_list)-1):
        new_list[x+1] = func(new_list[x], new_list[x+1])
        x += 1
    return new_list[len(new_list)-1]
