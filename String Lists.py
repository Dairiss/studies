#http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

#a=input("Write a string: ")
a="ababababca"
i=0
j= len(a) - 1

check = True

while i<=j:
	if (a[i]!=a[j]):
		check = False
		break
	else:
		i+=1
		j-=1
if check:
	print("This string is palindrom")
else:
	print("This string isnt palindrom")