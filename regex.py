import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.My number is 415-555-9999.')

areaCode, mainNumber = mo.groups() # multiple variablle asignment

for r in mo.groups():
    print(r)

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
# 'HaHaHaHaHa'
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# findAll() method
# search() returns the first match
# findAll() returns all matches, as lng as there are no groups

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
# '415-555-9999'

phoneNumRegexNoGroups = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # groups
phoneNumRegexWithGroups = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # has no groups
foo = phoneNumRegexNoGroups.findall('Cell: 415-555-9999 Work: 212-555-0000')
foo2 = phoneNumRegexWithGroups.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(foo)
print(foo2)
# ['415-555-9999', '212-555-0000']

str = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'

#  sub() // replace
reg = re.compile(r'\d+')
bar = reg.sub('X', 'There are 47 diamonds in my 7 bags')
print(bar)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
firstLetter = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(firstLetter)
# A**** told C**** that E**** knew B**** was a double agent.'

#  managing complex regexes

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    \d{3} # first 3 digits
    (\s|-|\.) # separator
    \d{4} # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )''', re.VERBOSE)

