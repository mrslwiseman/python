tableData = [
    ['apples', 'oranges', 'cherries', 'bananas'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]
def printTable(data):
    for cell in range(len(data[0])):
        longestWord = 0
        for line in data:
            for x in line:
                if len(x) > longestWord:
                    longestWord = len(x)
        for line in range(len(data)):
            print(data[line][cell].rjust(longestWord), end=" ")
        print()

printTable(tableData)
