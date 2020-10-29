import requests

first_response = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
data = str(first_response.text)
while not data.startswith('We'):
    next_response = requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+data)
    data = str(next_response.text)
    print(data)


# count = 0
# for line in data.splitlines():
#     count += 1
# print(count)

