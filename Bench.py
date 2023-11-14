import timeit
import matplotlib.pyplot as plt

def factorielClassique(n):
    result = 1
    while n>0:
        result *= n
        n -= 1
    return result

def factorielRecursive(n):
    if n > 0:
        return n*factorielRecursive(n-1)
    else:
        return 1

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return  fib(n-1)+fib(n-2)

if __name__=='__main__':
    tpsCl = []
    tpsRl = []
    tpsFi = []
    cbm = 40
    for i in range(cbm):
        tpsFi.append(timeit.timeit("""fib(i)""", number=1, globals=globals()))
        tpsCl.append(timeit.timeit("""factorielClassique(i)""", number=1, globals=globals()))
        tpsRl.append(timeit.timeit("""factorielRecursive(i)""", number=1, globals=globals()))


    fig = plt.figure()

    ax = fig.add_subplot(2, 1, 1)
    line = ax.plot(list(range(0, cbm, 1)), tpsCl, color='blue')
    line2 = ax.plot(list(range(0, cbm, 1)), tpsRl, color='red')
    line3 = ax.plot(list(range(0,cbm,1)), tpsFi, color='green')
    plt.show()
