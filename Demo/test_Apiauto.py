import requests
import json

def test_postreq():
    urls = "https://jsonplaceholder.typicode.com/posts"
    f = open("C:\\Users\\Akshay\\Documents\\API Automation\\pst\\demo.json", "r")
    pr = json.loads(f.read())

    resp = requests.post(urls, pr)
    print(resp.status_code)
    assert resp.status_code == 201