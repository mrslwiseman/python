def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("invalid argument")

print(spam(12))
print(spam(2))
print(spam(0))
print(spam(2))