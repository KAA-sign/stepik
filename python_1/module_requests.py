

import requests

response = requests.get('https://stepic.org/media/attachments/course67/3.6.2/662.txt')

data = response.text

count = 0
for line in data.splitlines():
    count += 1
print(count)
    