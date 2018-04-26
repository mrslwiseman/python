# for magician in magicians:
    # print("the magician is: {}".format(magician))

for value in range(1,5):
    print(value) # prints 1, 2, 3, 4

numbers = list(range(1,5))

odd_numbers = list(range(1,11,2)) # skip every 2 

print(numbers) # [1,2,3,4]
print(odd_numbers) # [1,2,3,4]

squares = []

for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)
print("min ", min(squares))
print("max ", max(squares))
print("sum ", sum(squares))

