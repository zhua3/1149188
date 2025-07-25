print ("Hello Python") #Output message

a = "Yo!" #String variable requires ""
b = "Wassup Alice!" 
c = 2 #Interger variable doesn't need ""
d = 4 
if 4<2:
	print (a) #Indentation represents a block of code/function
else:
	print (b) 
	

x = "a" #Either '' or "" will work just the same
y = "A"
print (x)
print (y)


a = 6
A = "Alice"
print (a) 
print (A) #A doesn't over write a, as python is case sensitive


x = str(3) #x will be "3"
y = int(3) #y will be 3
z = float(3) #z will be 3.0
print (x)
print (y)
print (z)
print (type (x))
print (type (y))
print (type (z))

my_var = 8 #variable names can only start with alphanumberic or underscore
alice_zhu = 6
print (alice_zhu)

x, y, z = "blueberry", "grape", "peach" #Many values to multiple variables
print (y)
print (x)
print (z)


x = y = z = "grape" #One value to multiple variables
print (x)
print (y)
print (z)


fruits = ["blueberry", "grape", "peache"] #Pack a collection of values
x, y, z = fruits #Unpack variables
print (x)
print (y)
print (z)


a = "Alice"
b = "is"
c = "awsome"
d = "who"
e = 2
print (a,b,c)
print (a, b, c) #Having space between values in the input doesn't affect the output style
print (d + b + a) #Due to lacking of a space after the variable words, output is squashed together
print (a, b, e) #Using comma works for mixed variable types
#Using '+' doesn't work for mixed variable types. Can't produce output


x = "cool" #global/outside variable
def myfunc(): #define a function named myfunc
	print ("Alice is", x)
myfunc()


x = "cool" #global/outside variable
def myfunc():
	x = "fantastic" #Local/inside variable
	print ("Alice is", x) #Output using local/inside variable
myfunc()
print ("Alice is", x) #Output using global/outside variable


def myfunc():
	global x #
	x = "crazy"
	print ("Alice is", x)
myfunc()


x = "nice" #Global variable
print ("Alice is", x) #Output using global variable
def myfunc ():
	global x
	x = "pretty" #Altering global variable within local function
	y = "crazy" #Local variable
	print ("Alice is", x, y) #Out put using altered global variable and local variable
myfunc()













