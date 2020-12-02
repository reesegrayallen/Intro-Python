# Reese Allen  rga2uz   CS1110-004  Apostolellis


import urllib.request


def instructors(department):
    """
    :param department: determines which department url will be opened from Lou's List and sorted through
    :return: alphabetically-sorted list containing each instructor listed in Lou’s List for the given department
    """
    url = "http://cs1110.cs.virginia.edu/files/louslist/" + department
    lou = urllib.request.urlopen(url)
    instructor_list = []
    for line in lou:
        row = line.decode('utf-8').strip().split("|")
        if "+" in row[4]:
            name = row[4] = row[4][0:row[4].index("+")]
            if name not in instructor_list:
                instructor_list.append(row[4])
        elif row[4] not in instructor_list:
            instructor_list.append(row[4])
    instructor_list.sort()
    return instructor_list


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    """
    :param dept_name: determines which department url will be opened from Lou's List and sorted through
    :param has_seats_available: if True, check to ensure that seats are available in the class; if False, ignores current enrollment
    :param level: the level of the desired class; if None, ignores class level
    :param not_before: limits start time of classes in list to time at which classes must start after or at
    :param not_after: limits start time of classes in list to time at which classes must start before or at
    :return: list of lists which contains all the information for all the classes that meet the provided criteria
    """
    dept_url = "http://cs1110.cs.virginia.edu/files/louslist/" + dept_name
    lous = urllib.request.urlopen(dept_url).readlines()
    total_list = []

    for line in lous:
        row = line.decode('utf-8').strip().split("|")
        total_list.append(row)

    seat_list = []
    if has_seats_available:
        for element in total_list:
            if int(element[15]) < int(element[16]):
                seat_list.append(element)
    else:
        for element in total_list:
                seat_list.append(element)

    level_list = []
    if level:
        number = str(level)
        number_low = str(number[0]) + "000"
        number_high = str((int(number[0]) + 1)) + "000"
        for element in seat_list:
            if int(number_low) <= int(element[1]) < int(number_high):
                level_list.append(element)
    else:
        for element in seat_list:
            level_list.append(element)

    before_list = []
    if not_before:
        b_time = not_before
        for element in level_list:
            if int(element[12]) >= b_time:
                before_list.append(element)
    else:
        for element in level_list:
            before_list.append(element)

    after_list = []
    if not_after:
        a_time = not_after
        for element in before_list:
            if int(element[12]) <= a_time:
                after_list.append(element)
    else:
        for element in before_list:
            after_list.append(element)

    return after_list



