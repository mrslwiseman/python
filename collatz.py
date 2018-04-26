def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

try:
    n = input('n: ')
    while collatz(int(n)) != 1:
        n = input('n: ')
except ValueError:
    print('Invalid Input')

