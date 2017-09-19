#http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        print(a)



#a = int(input("Give me a number: "))
a = 10

fib(a)
