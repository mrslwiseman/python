items = {
    'strawberries': 12,
    'cream': 8,
    'pears': 3,
    'peaches': 8
}

for k, v in items.items():
    print(k.ljust(20, '.'), end="")
    print(str(v).rjust(5, ' '))