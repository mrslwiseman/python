inventory = {
    'rope': 1,
    'arrow': 12,
    'gold coins': 42,
    'torch': 6,
    'dagger': 1
    }

def displayInventory(inv):
    count = 0
    for k, v in inventory.items():
        print(v, k)
        count += v
    print('Total number of items: ' + str(count))

displayInventory(inventory)