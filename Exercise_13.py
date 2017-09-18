#http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html


def fib(a):
    i = 1
    j = 1
    print(i,j,end=" ")
    for k in range(a):
        c = i
        i += j
        j = c
        print(i,end=" ")



#a = int(input("Give me a number: "))
a = 10

fib(a)
