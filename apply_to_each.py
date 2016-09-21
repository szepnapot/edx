def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]


def multBy5(e):
    return e * 5

applyToEach(testList, lambda e: e + 3)

print(testList)