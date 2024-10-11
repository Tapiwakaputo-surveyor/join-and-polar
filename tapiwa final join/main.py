def join_variables():
    import math
    variablex1 = float(input('enter x1 coordinate:'))
    variablex2 = float(input('enter x2 coordinate:'))
    variabley1 = float(input('enter y1 coordinate:'))
    variabley2 = float(input('enter y2 coordinate:'))
    differenceX= variablex2-variablex1
    differenceY= variabley2-variabley1
    r          = math.sqrt(differenceY**2 + differenceX**2)
    Q          = math.degrees(math.atan(differenceY/differenceX))
    print(r)
    print(Q)
join_variables()

