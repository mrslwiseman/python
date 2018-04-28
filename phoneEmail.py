import re, pprint, pyperclip

text = pyperclip.paste()

def p(s):
    pprint.pprint(s)

emailRegex = r'([a-zA-Z0-9.]+@[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,4}))'
phoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))? # area code
    (?:\s|-|\.)? # separator
    (\d{3}) # first 3 digits
    (?:\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    ''', re.VERBOSE)

# search text for emails
# search text for phone numbers

emails = re.compile(emailRegex)
numbers = re.compile(phoneRegex)

matches = []

for groups in numbers.findall(text):
    phoneNum = '-'.join([groups[0], groups[1], groups[2]])
    matches.append(phoneNum)

for groups in emails.findall(text):
    matches.append(groups)

for item in matches:
    print(item)

# Contact Us

# No Starch Press, Inc.
# 245 8th Street
# San Francisco, CA 94103 USA
# Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
# Fax: +1 415.863.9950

# Reach Us by Email

#     General inquiries: info@nostarch.com
#     Media requests: media@nostarch.com
#     Academic requests: academic@nostarch.com (Please see this page for academic review requests)
#     Help with your order: info@nostarch.com 

# Reach Us on Social Media

#     Twitter
#     Facebook