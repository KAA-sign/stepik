import requests

response = requests.get('https://stepic.org/media/attachments/course67/3.6.2/726.txt')

data = response.text

count = 0
for line in data.split:
    count += 1
print(count)
    