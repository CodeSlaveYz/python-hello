import os


PORT = 8081
name = os.environ['NAME']
if name == None :
  name = "world"
MESSAGE = "Hello," + name + "!\n"
