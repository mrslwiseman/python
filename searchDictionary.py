import re
# todo : speed: prevent search going past first letter of search input
# eg. 'ABACUS'
    # find index of first B word
    # search up to that index

fo = open("dictionary.txt", "r")
words = fo.read()
search = input('Word to search for:').upper()
regex = re.compile(r'(([^- ]\b)' + search + r'\n((.|\n))+?(\n{2})(?:(?=[A-Z]{2}\w)))')

foo = regex.search(words)

if (foo == None):
    print(search, ' was not found, did you spell it correctly?')
else:
    print('Found. \n\n')
    print(foo.group(1))
    print('\n\n')
