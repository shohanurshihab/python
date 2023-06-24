#Trying comment 
"""
identeation
comment styles
"""
print('1st')
if 2>1:
 print("Hello, World") # identation must for logic and code to work

# in py no need to specify type
X = 7 # variables are case sensetive A & a are different
x = float(9) # type specified by casting operator
y = "Mahdi" # single'' or double"" quote doesn't matter in py  


print(X)
print(x)
print(y)
print(type(X),type(x),type(y)) # using type() function to get variable type 
print()


# variable names should be alpha_numeric & underscore_ and must start with a letter or underscore 

print('2nd')
_var = 5
var1 = 6
var_3 = 1
print(_var,var1,var_3)

myVar = 8 # Camel case _each word in variable name starts with capital except first word
MyVar = 8 # Pascal case _Each word starts with a capital letter
My_Var = 8 #Snake Case _Each word is separated by an underscore character 
print()


print('3rd')
# assigning multiple variables in one line
q, w, e =7,8,9 # both side should have equal amount of counterparts
print(q)
print(w)
print(e)
print()

#one value to multiple variables at one line
print('4th')
r = t = y = "Aam"
print(r)
print(t)
print(y)
print()



# unpacking = extracting values from the list,tuples,etc and assign them to variables
print('5th')
fol = ["Lichu",'Boroi','Tormuj'] # both side should have equal amount of counterparts
u, i, o = fol
print(type(fol)) 
print(u,i,o)
print()



# comma, and plus + operator are used to output multiple variable
print('6th')
print(u+i+o) # requires space after each value when assigning
print(u,i,o) # no space required
print()

# output multiple type variables using comma not plus operator
print('7th')
p = 5
a = 'string'
print(p,a)
s=5
print(p+s) # + plus operator acts as a mathematical operator for numbers
print()

# global variable uses and keyword
print('8th')
d = "start" # global variable
print(d)

def fun():
 d ="stop" # here is local variable which replace the global  
 global f # variable belongs to global using global keyword even inside a function 
 f= "initiate"
 print(d)

fun() #calling function
print(f) # implementation of global keyword
print()

# variable types tryout
print('9th')
g = 5j # complex
print(type(g)) 
h = tuple(("apple", "banana", "cherry")) #tuple
print(type(h))
j = range(7) #range
print(type(j),j)
k = dict(name = "John", age = 36) # mapping
print(type(k),k)
l = set(("apple", "banana", "cherry")) # set
print(type(l),l)
z = frozenset(("apple", "banana", "cherry")) # set
print(type(z),z)
c = bool(5<0) # boolean  
print(type(c),c)
#Binary Types
#v = b"hello"
v = bytes(5)
print(type(v),v)
b = bytearray(5)
print(type(b),b)
n = memoryview(b"h")
print(type(n),n)
print()

#numeric types
print('10th')
m = -.35e3
print(m,type(m))
M = 3+5j
print(M,type(M))
N = int(m) # float2int
print(N,type(N)) 
B = complex(N) # int2complex
print(B,type(B))
# int2complex & float2complex not possible

import random
print(random.randrange(1, 10))
print()

#casting
print('11th')
V =int('5')
print(V)
#string multiline using three ' or "
C = """The little girl from the front apartment
said,"Dad,Can we have it?"."""
print(C)
print(C[2],'\n') #strings are arrays and its element can be accessed by [] brackets
for x in 5:
  print(x)
print('\n',len(C)) #len() to determine length of a string
