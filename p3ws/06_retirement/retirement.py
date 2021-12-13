def calculateRetirement(age, saving, work, retire):
    year = age // 12
    month = age % 12
    for i in range(work[0]):
        print('Age {:3d} month {:2d} you have ${:.2f}'.format(year,
                                                              month, saving))
        saving = saving + saving * work[2] + work[1]
        age += 1
        year = age // 12
        month = age % 12
        pass
    for j in range(retire[0]):
        print('Age {:3d} month {:2d} you have ${:.2f}'.format(year,
                                                              month, saving))
        saving = saving + saving * retire[2] + retire[1]
        age += 1
        year = age // 12
        month = age % 12
        pass
    return 0


def main(a, b, c, d):
    calculateRetirement(a, b, c, d)


if __name__=="__main__":
    age = 327
    saving = 21345
    work = (489, 1000, 0.045 / 12)
    retire = (384, -4000, 0.01 / 12)
    main(age, saving, work, retire)
    pass
