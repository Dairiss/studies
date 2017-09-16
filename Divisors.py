#http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
#a=int(input("Choose a number: "))
a=100

x=list(range(2, a // 2 + 1))

divisors= []

for i in x:
	if (a % i==0):
		divisors.append(i)
print(divisors)