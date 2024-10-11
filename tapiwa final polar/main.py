def polar_variables():
    import math
    YA = float(input('enter YA coordinate Y'))
    XA = float(input('enter XA Ccoordinate X'))
    D  = float(input('enter distance:'))
    V  = float(input('enter bearing:'))
    r  = (V/180)*math.pi
    YB = YA + D*math.sin(r)
    XB = XA + D*math.cos(r)
    print(f'YB coordinate:{YB}')
    print(f'XB coordinate:{XB}')
polar_variables()