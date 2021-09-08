# gpy
# Your can take a look at the tests
# in "test_exercises", but do not need to
# change anything there.
#
# To run the tests, you will need to install
# a couple of python libraries. You can
# install this by running:
# "python3 -m pip install -U --user pytest pytest-xdist".
# Once you have it installed:
# You can run the tests with:
# "pytest -f --color=yes --looponfail"
# from the terminal, inside this folder.

#
# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#

#
# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#

#
# 3)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted, it returns None.
#

#
# 4)
# Create a function named "greet_person". It should
# accept a string as an argument and return that
# string as part of a longer sentence that says hello:
# i.e. "Sophia" --> "Hello, Sophia!"
# If the function is called with an argument that is
# not a string, it should return "Please provide a name."
# i.e. 5 --> "Please provide a name."
#

# 1)

def triple(x):
    y = 3*x
    return y

#x=int(input("Value of which we want its triple: "))
x=3
valor1=triple(x)
print("1r valor = ", valor1)

# 2)

def substract(a,b):
    z = b-a
    return z
#a=int(input("First substract parameter is "))
#b=int(input("Second substract parameter is "))
a=2
b=1
valor2=substract(a,b)
print("2o valor = ", valor2)


# 3)
def safe_substract(c,d):
    try:
        return d-c
    except TypeError:
        return None

valor3 = safe_substract(2, '1')
print("3r valor = ", valor3)

# 4)  
def greet_person(e):
    try:
        return 'Hello, ' + e + '!'
    except TypeError:
        return 'Please provide a name'

valor4 = greet_person('Sophia')
print(valor4)
