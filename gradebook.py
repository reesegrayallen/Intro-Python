#  Reese Allen  rga2uz     CS1110-004  Apostolellis


my_dict = {}
count = {}


def assignment(kind, grade, weight=1):
    """
    :param kind: a string which indicates the type of assignment (exam, hw, or lab)
    :param grade: an integer representing the grade received on the assignment (param kind)
    :param weight: indicates how much weight this assignment has compared to to others of its kind
    """
    my_dict[kind] = my_dict.get(kind, 0) + grade * weight
    count[kind] = count.get(kind, 0) + weight


my_list = []


def total(proportions):
    """
    :param proportions: references the syllabus, which provides the weight for each group of like assignments
    :return: total grade in the class
    """
    grade = 0
    for i in proportions:
        my_list.append(i)
    for n in range(len(my_list)):
        if my_list[n] not in my_dict:
            my_dict[my_list[n]] = 0
            count[my_list[n]] = 0
    for i in proportions:
        if count[i] != 0:
            grade += my_dict[i] / count[i] * proportions[i]
        else:
            pass
    return grade
