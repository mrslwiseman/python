import sys, pyperclip
# an insecure password storage application.

PASSWORDS = {
    "twitter": "password123"
}

request = sys.argv[1]

if len(sys.argv) < 2:
    print("Usage: ./pw.py [account] - copy account password to clipboard")
    sys.exit()

if request in PASSWORDS:
    pyperclip.copy(PASSWORDS[request])
    print(request.title() + " password copied successfully")
else:
    print('There is no account: ' + request)