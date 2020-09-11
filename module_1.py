#!/usr/bin/python3

import requests

response = requests.get('https://stepic.org/media/attachments/course67/3.6.2/726.txt')
line_count = 0
with open(response.text) as f:
    for line in f:
        line_count += 1
print(line_count)

