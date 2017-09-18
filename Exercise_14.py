#http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

def using_set(a):
    return list(set(a))

def using_loop(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y


#a = [int(i) for i in input().split()]
a = [5, 10, 15, 20, 25, 5, 10, 15, 20]
print(a)

c = using_loop(a)
print(c)


b = using_set(a)
print(b)
