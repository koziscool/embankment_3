
def e2():
    fibo = [1, 2]
    while fibo[-1] < 4 * 10 ** 6:
        fibo.append( fibo[-2] + fibo[-1] )
    total = 0
    for f in fibo:
        if f % 2 == 0:
            total += f

    return total

if __name__ == '__main__':
    print e2()


