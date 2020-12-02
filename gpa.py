# Reese Allen rga2uz  Apostolellis CS1110-004 

course_total = 0
gpa_total = 0


def add_course(g, c=3):
    global course_total
    global gpa_total
    course_total += c
    gpa_total += g * c


def gpa():
    return gpa_total / course_total


def credit_total():
    return course_total

