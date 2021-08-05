import os


PORT = 8080
name = os.environ['NAME']
if name == None :
  name = "world"
MESSAGE = "Hello," + name + "!\n"
