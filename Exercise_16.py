#http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
import random



def password(a):
    w = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
    s = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=',';',':','>','<','/','?','|',',','.']
    newpass = []
    for i in range(a):
        c = random.randrange(3)
        if (c == 0):
            k = random.randrange(52)
            newpass.append(w[k])
        elif (c == 1):
            k = random.randrange(23)
            newpass.append(s[k])
        else:
            newpass.append(random.randrange(10))
    for i in newpass:
        print(i,end='')
    print()





#a = int(input("Give me a number: "))

a = 20

password(a)
