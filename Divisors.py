#http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
#a=int(input("Choose a number: "))
a = 100

xs = range(2, a // 2 + 1)

print([x for x in xs if a % x == 0])
