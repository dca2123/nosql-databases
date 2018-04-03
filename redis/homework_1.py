# written in python3. May need to pip intall requests, although probably not
import requests
import ast

#http request
s =  requests.get("https://api.nasa.gov/planetary/apod?api_key=2SpOXDx3rOunTdmn9GQS0ShJSfoC8p7pLJ0LgMDK&date=2017-09-26")
#convert the string to a python dictionary
d = ast.literal_eval(s.text)

#get the url from the string
url = d["url"]
#print the url
print(url)

