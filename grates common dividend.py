def list_comprehension():
    m = int(input())
    n = int(input())
    factor_of_m = []
    factor_of_n = []
    cf = []
    for i in range(1, m + 1):

        if m % i == 0:
            factor_of_m.append(i)
    print(factor_of_m, end=" ")

    for j in range(1, n + 1):

        if n % j == 0:
            factor_of_n.append(j)
    print(factor_of_n, end=" ")
    # factor_of_m.extend(factor_of_n)
    # print(factor_of_m)
    for f in factor_of_m:
        if f in factor_of_n:
            cf.append(f)
    print(cf)
    print(cf[-1])


list_comprehension()
