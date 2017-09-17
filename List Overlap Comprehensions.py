#http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
import random

k = random.randint(1,20)
a = random.sample(range(1,30), k)
k = random.randint(1,20)
b = random.sample(range(1,30), k)
a.sort()
print(a)
b.sort()
print(b)

result = [i for i in set(a) if i in set(b)]
print(result)
