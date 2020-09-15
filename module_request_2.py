#!/usr/bin/python3

import requests

first_response = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')

data = str(first_response.text)
print(data)
while not data.startswith('We'):
    next_response = requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+data)


# count = 0
# for line in data.splitlines():
#     count += 1
# print(count)

