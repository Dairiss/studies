#http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
import random

a = input()
b = random.randint(1,9)
i = 0

while (a != "exit"):
    if(int(a) < b):
        print("You number too low")
        i += 1
    elif (int(a) > b):
        print("You number too high")
        i += 1
    else:
        print("Right!",a)
        print("You took only",i,"tries")
        print("If you want continue write another number or exit")
        b = random.randint(1,9)
    a = input()
