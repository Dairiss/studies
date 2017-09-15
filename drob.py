def gcd(a,b):
    r = b % a
    while(r != 0):
        b = a
        a = r
        r = b % a
    return a


def main():
    n = int(input('n = '))
    r = i = 0
    while (r != 1):
        if (n % 2 == 0):
            a = n // 2 - 1 - i
        else:
            a = n // 2 - i
            i += 1
            b = n - a
            r = gcd(a, b)

    print('a / b = ', a, '/', b) 


if __name__ == '__main__':
    main()
