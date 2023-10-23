multL = lambda a, b, c: a * b * c
resLambda = multL(2, 5, 5)


def test(a, b, c):
    return a * b * c


print(resLambda)
print(test(2, 3, 4))

L = [8, 15, 7, 3, 11, 23, 187, -5, 20, 17]

LTest = lambda l: [num for num in l if 10<num<20]
print(LTest(L))
