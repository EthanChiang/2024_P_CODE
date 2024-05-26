import requests

url ="https://www.ptt.cc/bbs/NBA/index.html"

response = requests.get(url)
# print(response.text)
with open("output.html",'w',encoding="utf-8") as f:
    f.write(response.text)