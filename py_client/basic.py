from django import http
from requests import *

url='http://127.0.0.1:8000/api'

getresponse=get(url)

print(getresponse.json())