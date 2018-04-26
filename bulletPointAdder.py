# paste from clipboard
import pyperclip
x = pyperclip.paste().split("\n")

for i in x:
    x[i] = "* " + x[i]

print(x)