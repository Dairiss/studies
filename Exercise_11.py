#http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
def is_prime(number):
    '''Returns True for prime numbers, False otherwise'''
    #Edge Cases
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    #All other primes
    else:
        prime = True
        for check_number in range(2, (number // 2)+1):
            if number % check_number == 0:
                prime = False
                break
    return prime


a = int(input("Give me a number: "))

check = is_prime(a)
if check:
    print("You number is prime")
else:
    print("You numer not a prime")
