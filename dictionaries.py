d = {
    'name':'matt',
    'age':28,
    }

for i in d.items():
    print(i[0]) # name
    print(i[1]) # 'matt'

for k, v in d.items():
    print('key:', k, 'value:', v)

for v in d.values():
    print(v)

for k in d.keys():
    print(k)

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

x = 'name' in d.keys()
print(x) # true

picnicItems = {
    'apples':5,
    'cups':2    
    }

# get()
print('there are ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
