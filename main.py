import requests

text=requests.get('https://vk.com/').text
print(text)