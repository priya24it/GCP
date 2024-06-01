import requests

url = 'http://127.0.0.1:5000/incomes'
print(url)
myobj = ''
# myobj = {'somekey': 'somevalue'}
# myobj = 'abc'
# x = requests.get(url=url,data=myobj)
header = {"Content-Type": "application/json"}
x = requests.post(url=url,headers=header,data=myobj)
print(x.status_code)
print(x.text)
# print(x.get())

# x = requests.post(url, json = myobj)

# print(x.text)