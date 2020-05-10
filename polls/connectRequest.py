import requests

url = 'https://www.baidu.com'


def getBaiduTest():
    respond = requests.get(url)
    # print(respond.text)
    return respond


def getHelloApi():
    respond = requests.get("http://localhost.:8080/hyz/test/helloWorld")
    return respond
