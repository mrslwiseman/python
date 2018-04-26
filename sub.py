import re
reg = re.compile(r'(fuck(?:en|ing)?|shit|cunt)', re.I) # ?: non-capturing group
rudeString = 'You are a piece of fucken shit. Go fuck yourself. You shit cunt. Fucken hell.'

foo = reg.findall(rudeString)
print(foo)

bar = reg.sub('@#*!', rudeString)
print(bar)


