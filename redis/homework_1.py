# make sure to "pip install requests"
import requests
import ast

s =  requests.get("https//api.nasa.gov//planetary/apod?api_key=2SpOXDx3rOunTdmn9GQS0ShJSfoC8p7pLJ0LgMDK") #&date=2017-09-26")
print(s)
print("\n")

d = ast.literal_eval(s)
print(d)

url = d["url"]
print("\n")
print(url)

