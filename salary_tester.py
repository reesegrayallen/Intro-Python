import salary

for name in (
        'Teresa Sullivan',
        'Sullivan, Teresa',
        '161048349',
        'Ali Reza Forghani Esfahani',
        'pamela-neff',
        'Thomas Jefferson'
        ):
    job, money, rank = salary.report(name)
    print(name, 'is a', job, 'and makes', money, '(rank', str(rank)+')')



# Teresa Sullivan is a President University of Virginia and makes 754830.0 (rank 1)
# Sullivan, Teresa is a President University of Virginia and makes 754830.0 (rank 1)
# 161048349 is a Multimedia Creative Technician and makes 33000.0 (rank 0)
# Ali Reza Forghani Esfahani is a Lab Specialist 3-LAB49 and makes 62745.0 (rank 4015)
# pamela-neff is a Laboratory & Research Spec II and makes 58496.0 (rank 4365)
# Thomas Jefferson is a None and makes 0 (rank 0)