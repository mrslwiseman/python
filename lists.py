bicycles = ['trek', 'cannondale', 'redline', 'specialized']

bicycles[0] = 'giant'

bicycles.index('cannondale')
# 1


if 'trek' not in bicycles:
    print('Noooo get a trek!')



if 'specialized' in bicycles:
    print('Yesssss Specialized!!')

print("there are {} bicycles in my array".format(len(bicycles)))

bicycles.append("malvern star")

bikes = ["ducati", "honda", "yamaha"]

# insert at position 1
bikes.insert(1,"kawasaki")
# delete items
del bikes[0]

print(bikes)

# removes item at number 1
foo = bikes.pop(1) # honda
bar = bikes.remove("honda")


bikes = ["ducati", "honda", "yamaha"]

# print(bicycles[0]) # trek

# for i in bicycles:
#     print(i) # prints each name of bicycle

# for i in range(10):
#     print(i) # prints 0 through 9

# for i in range(len(list)):
    # do something

cat = ['fat', 'black', 'timid']
size, color, disposition = cat