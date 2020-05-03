def persistence(n):
    n = str(n)
    y = 0
    while len(n) > 1:  
        m = 1
        y +=1
        for i in n:
            m *= int(i)
        n = str(m)
    return y