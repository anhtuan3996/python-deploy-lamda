import requests

def call_pylennin(event=None, context=None):
    r = requests.get("https://pylenin.com")
    if r.status_code == 200:
        return "It was successful"
#print(call_pylennin())