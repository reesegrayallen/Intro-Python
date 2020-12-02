import urllib.request
import re

stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/emails.html')

email_list = []
for line in stream:
    decoded = stream.readline().decode('utf-8').strip()
    emailhunt = re.compile(r'')
    temp_list = emailhunt.findall(decoded)
    for element in temp_list:
        email_list.append(element)

for element in email_list:
    if "NOSPAM" in element:
        element.replace("NOSPAM", "")
    print(element)

