from pprint import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    if character.isalpha():
        count.setdefault(character, 0)
        count[character] = count[character] + 1

# create an array of tuples from the count dictionary
items = list(count.items())

# sort by the count
foo = sorted(items, key=lambda c:c[1], reverse=True)
print(foo)
print('The most common letter is', foo[0][0].title(), 'which occured', foo[0][1], 'times.' )
# print(type(items[0])) #tuple
pprint(count)