# Lesson 2
# Taking a step back after the deep dive of the first lesson 

# Showing how to interact with Python:
# https://realpython.com/interacting-with-python/#hello-world

"""
How to run Python code?

You can execute Python code in two ways:

- Write code to a file, then execute it
    - https://realpython.com/interacting-with-python/#running-a-python-script-from-the-command-line
- Interact with the interpreret interactively
    - see https://realpython.com/interacting-with-python/#using-the-python-interpreter-interactively

DEMO: 
- show both in Mac Terminal program
  - print some text
  - use Python as a calculator

In Repl.it, you can do both of those: you can type to a file and execute it, or you can type directly in to the interactive interpreter on the right hand side.
Repl.it makes it easy to write, share and collaborate on code, that's why we use it - you can install Python on your computer if you want to. 
Later, we might do more complex exercises that way. 

RECAP - What have we learned on the first session

## Whitespace

- Whitespace is meaningful
- It is used for "indentation": we create blocks of code that belong together. For instance, we use indentation to separate the body of a function from the rest of the code.
- Spaces and tabs (you can use either one, just be consistent - it's best to use four spaces)

## Comments

- Comments are not executed by the interpreter
- Comments are written after the # symbol, or betweenn triple quotes (especially multi-line comments)

## Data types 

### We had a look at a few types of data:

- int
    "whole numbers"
    Example: 1, 7, 42
- float
    numbers with decimal point
    Example:  0.2, 5.0, 21972.129871
- boolean
    Values representing "Boolean logic": True/False. 
    True and False are the only boolean values.
- strings
    Textual data types. They are between single or double quotes/
    Example: "padlizsankrém", 'spagetti', 'rántott hús'
    Multi-line strings can be defined between triple quotes.

(We will look at other types of data a bit later.)

### The type() built-in function

You can check the data type of a value using the built-in "type" function:
- type('pizza') will tell you that 'pizza' is a string, 
- type(1.0) will tell you that 1.0 is a float.

## Variables

Varialbes hold some kind of data. 
To define a variable, you just have to type the name of the variable, and equality sign, and the value of it:

my_favourite_food = 'anything except coriander!'

The equality sign here stands for the "assignment" - we assign the string 'anything except coriander!' to the variable my_favourite_food

Variables are used to store data in your program, so that you can re-use them later.

## Functions

We can write functions to make our code re-usable. For example, we might want to reuse a function that calculates some value based on some input.

We use the def keyword to define a function.

## Operators

+, -, /, //, *, **, %

# New stuff

- built-in keywords in Python
There are a few keywords in Python which are reserved for special purposes. They cannot be used are variable names. 

Some keywords are:

- True, False
- def, return
- if, else
- for, while, continue, break

See the full list at https://docs.python.org/3/reference/lexical_analysis.html#keywords

## type casting

You can try to "cast" a variable into another type.

For instance:

int('10')
str(10)

## boolean logic

and, or, not, is,

in

These operators return boolean values

truthiness - we'll look at it later

## strings

- len()
- indexing, slicing
- concatenating
- multiplying
- lower(), upper(), capitalize()
- count()
- startswith(), endswith()
- in
- isdigit()

## control flow

if/else statements

a = 2
b = 3

if a == 2:
    print(a)

if a == 2:
    print("two")
    if b == 3:
        print("b is 3") 
else:
    print("other")

if a == 2 and b == 3:
    print("b is 3")
    

a = 1    
b = 2

if a == 1:
    print("one")
elif b == 2:
    print("two")
else:
    print("a lot")


## lists
"""

def simple_function(n):
    return n ** 3

def print_function(n):
    print( n**3 )

my_variable = 3 

cube_of_my_variable = simple_function(my_variable)

print('END OF FILE')

