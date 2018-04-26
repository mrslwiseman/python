def displayInventory(inv):
    count = 0
    for k, v in inv.items():
        print(v, k)
        count += v
    print('Total number of items: ' + str(count))


def addToInventory(inv, loot):
    new_inv = inv.copy()
    for i in loot:
        new_inv.setdefault(i, 0)
        new_inv[i] += 1
    return new_inv

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
