print('Enter number of rooms:\n')
n=int(input())
print('Enter the number of occupied rooms\n')
k=int(input())
if (k==0 or k==n): print('0 0\n')
else:
	if (k == n // 2): c = k
	elif (k < n // 2): c = k + 1
	else: c = n - k
	print('1 ',c, '\n')