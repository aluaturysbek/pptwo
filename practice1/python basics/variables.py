x = 5
y = "Hello, World!"


#casting - stating new variables type
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


#getting var-s type
x = 5
y = "John"
print(type(x))
print(type(y))


x, y, z = "apple", "orange", "pear"



x = "awesome" #global var, outside the function

def myfunc():
  x = "fantastic" #local var inside the function
  print("Python is " + x)

myfunc() #will use local

print("Python is " + x) #will use global, as local isnt available for use outside the function

