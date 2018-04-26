# Comma Code
# Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats'. But your function
# should be able to work with any list value passed to it

def read(items):
    # for each item print, with a comma
    for i in range(len(items)):
        # if its the second to last print 'and' instead of comma
        if i == len(items) - 1:
            print('and', items[i], end=' ')
            break
        print(str(items[i]), end=', ')

read(spam)