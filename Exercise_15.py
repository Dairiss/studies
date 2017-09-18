#http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
def reverseString(a):
  return " ".join(a[::-1])


a = input().split()
print(reverseString(a))
