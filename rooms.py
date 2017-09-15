def main():
    print('Enter number of rooms:')
    n=int(input())
    print()

    print('Enter the number of occupied rooms')
    k=int(input())
    print()

    if (k == 0 or k == n):
        print('0 0')
    else:
        if (k == n // 2):
            c = k
        elif (k < n // 2):
            c = k + 1
        else:
            c = n - k
        print('result:', '1 ', c)


if __name__ == '__main__':
    main()
