"""
this is a multiline 
comment
"""

spam = "Hello World"
print("Hello" in spam) # true
print("Whats" not in spam) # true

print(spam[:5]) # Hello

print(spam.upper()) # HELLO WORLD
print(spam.lower()) # hello world
print(spam[0].isupper()) # true
print(spam[0].islower()) # false

spam.isalpha() 
spam.isalnum() 
spam.isdecimal() 
spam.isspace() 
spam.istitle() 
print(spam.startswith('Hello')) # true
print(spam.endswith('Hello')) # true

print(", ".join(['foo', 'baz']))
print("My name is Simon".split())

"Hello".ljust(20, '#') # '#############'Hello'
"Hello".rjust(20, '#') # 'Hello##############'
"Hello".center(20, '#') # '###########Hello############'

print("   Hello   .".lstrip())
# rstrip(), strip()2


