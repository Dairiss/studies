#http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html



#a=[int(i) for i in input().split()]
a = [5, 10, 15, 20, 25]

b=[a[-i] for i in range(0,2)]

print(b)
