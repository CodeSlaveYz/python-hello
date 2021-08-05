import os


PORT = 80
name = os.environ['NAME']
if name == None :
  name = "world"
MESSAGE = "Hello," + name + "!\n"
