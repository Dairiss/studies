#http://puu.sh/xBic2/3d2613a3d8.png
a=[]
k=0
while True:
    lst=input()
    if (lst == "end"):
        break
    a.append([int(i) for i in lst.split()])
    k+=1

k1=len(a[0])
b=[[0 for i in range(k1)] for j in range(k)]
for i in range(k):
    for j in range(k1):
        b[i][j] = a[(i-1) % (k)][j] + a[(i+1) % (k)][j] + a[i][(j-1)% (k1)] + a[i][(j+1)% (k1)]



for i in range(k):
    for j in range(k1):
        print(b[i][j], end=" ")
    print()
