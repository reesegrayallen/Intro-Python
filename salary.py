# Reese Allen rga2uz   CS1110-004

import urllib.request
import re


def report(name):
    """

    :param name: the name of the person you are searching for information on
    :return: that person's job title, total salary, and salary rank within UVA (or 0 if not provided)
    """
    job, money, rank = None, 0, 0
    if name.find(",") != -1:
        change_name = name.strip().split(",")
        name = change_name[1][1:] + " " + change_name[0]
    name = name.lower().replace(" ", "-")
    try:
        link = urllib.request.urlopen("https://cs1110.cs.virginia.edu/files/uva2016/" + name)

    except:
        return None, 0, 0

    jobreg = re.compile(r"Job title: (.+)<br />")
    moneyreg = re.compile(r"total gross pay: \$(.+)\"")
    rankreg = re.compile(r"<td>([0-9,]+) of ([0-9,]+)</td></tr>")

    for line in link:
        decoded = line.decode('utf-8').strip()

        find_1 = jobreg.search(decoded)
        if find_1 is not None:
            job = find_1.group(1)
            if "&amp;" in job:
                job = job.replace("&amp;", "&")
            if "&lt;" in job:
                job = job.replace("&ly;", "&")
            if "&gt;" in job:
                job = job.replace("&gt;", "&")

        find_2 = moneyreg.search(decoded)
        if find_2 is not None:
            money = find_2.group(1)
            money = float(money.replace(",", ""))

        find_3 = rankreg.search(decoded)
        if find_3 is not None:
            rank = find_3.group(1)
            rank = int(rank.replace(",", ""))

    return job, money, rank





