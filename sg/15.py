for a in range(1000):
    f = True
    for x in range(100):
        for y in range(100):
            if not (((x ** 2 + y ** 2) < a) or (x > 3) or (y >= 5)):
                f = False
    if f:
        print(a)
        