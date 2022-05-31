from turtle import title
from django import http
from requests import *

url='http://127.0.0.1:8000/api/create'


data={
    "title":"hicham",
    "content":"hhhhhhhh",
    "price":144
}
getresponse=post(url,json=data)

print(getresponse.json())