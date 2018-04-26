# user copies text to clipboard
# runs the program

# require pyperclip
# program accesses clipboard, pastes
# search for phone numbers
# search for email addresses
# find all matches
# format matches into a single string to paste
# display message if error
import re
string = '''
*match:
mrslwiseman@gmail.com
0468 791 649
0468791649
+61468791649
+6463796406
08 7567 7468

*skip:
66 66 66
6 6
6
'''
phoneNumber = r'([+0?]4(([^\t\n\r])?\d+)+)'
regex = re.compile(phoneNumber)
foo = regex.findall(string)
print(foo)