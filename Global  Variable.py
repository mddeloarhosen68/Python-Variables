#Global Variables

#Ex:1
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()

#Ex:2
x = "awesome"
def myfunc():                   # Create a variable inside a function, with the same name as the global variable
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
