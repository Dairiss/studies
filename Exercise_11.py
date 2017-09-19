#http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
def is_prime(number):
    return not (
        number < 2
        or any(number % d == 0 for d in range(2, int(number / 2) + 1))
    )


a = int(input("Give me a number: "))

check = is_prime(a)

print("Your number is {}a prime number.".format("" if check else "not "))
