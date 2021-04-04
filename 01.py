"""
What is a program? 
Code, whitespace, comments, errors in Python

A program is a collection of instructions - we instruct the computer what to do, and it does exactly that
A program is executed line by line, one afer another, starting from the first line of a file. The "syntax" of a program follows a strict set of rules that the computer can understand
Python is one of many programming languages. It's very popular in many areas: 
- web development, 
- scientific computing, 
- bioinformatics (a straind of DNA as a sequence of characters)
- finance (financial analysis, stock trading)
- machine learning (image recognition)
- data science
- recommendation engines
- natural language processing (sentiment analysis, etc)
- gaming

A special program, called the interpreter, reads and executes our Python code
Python code is written into files ending with .py.

This text you are reading now is valid Python code.
"""

# Code looks like this:
cica = 'Mirci'

def miau():
    # indentation is the usage of spaces or tabs to create a function "body"
    print('Miauuuu!!!')

miau()

# Lines starting with # are comments
# These are not evaluated
# cica2 = "Mircike"
# asdasda zxcasda. 1q23123asda

def woof():  # Comments can be written inline, next to the code
    pass


def multiply_by_two(number):
    return number * 2

double_six = multiply_by_two(6)

"""
Lines between three quotation marks (") are comments too
These can be multi-line

Like this
"""

# Data types
# type()
# int, float, boolean, string... etc

# Variable
## naming style and capitalisation
## Assignment ("legyen egyenlő")

kutya = "Morzsi"

valtozo_neve = "ertek"

kutya2 = 'Bogi'

tanulok_szama = 10  # No Hungarian accents in variable names

tanulok_szama = tanulok_szama + 1 
tanulok_szama += 1

max_letszam = 15


"""
## Equality, comparison

kutya == kutya2 

1 == 2

1 == 1

2 > 1

comparison operators: ==, <, >, <=, >=
"""

# Functions

## Function definition

### "Indentation"
### Whitespace is important - make it 4 spaces 

### Function "calls"
### Returning things 
### Side effects
### Parameters (arguments)
#### Functions can be arguments too
#### A function can have many parameters
## variables as arguments
## print(name) vs. print("name")
## Assign variable from the return value

# Printing text

# Error messages

# If-else

# BONUS exercises


## Speciális karakterek

"""
Windows (magyar billentyűzet)


| Karakter | kód             | Karakter | kód             |
|----------|-----------------|----------|-----------------|
| [        | alt gr + F      | ]        | alt gr + g      |
| {        | alt gr + b      | }        | alt gr + n      |
| <        | alt gr + í      | >        | alt gr + y      |
| &        | alt + c         | \|       | alt + q, alt + w|
| *        | alt gr + -      | ;        | alt + ,         |
"""


"""
MAC (magyar billentyűzet)

| Karakter | kód             | Karakter | kód             |
|----------|-----------------|----------|-----------------|
| [        | alt + 8         | ]        | alt + 9         |
| {        | alt + 7         | }        | alt + ö         |
| <        | alt + shift + y | >        | alt + shift + x |
| &        | alt + 1         | \|       | alt + í         |
| *        | alt + shift + , | ;        | alt + .         |
"""

# Reading

"""
OPTIONAL: https://realpython.com/installing-python/
OPTIONAL: https://realpython.com/interacting-with-python/
https://realpython.com/python-data-types/
https://realpython.com/python-variables/
"""


# OPTIONAL Homework on Codewars - these might include material that we have not covered yet

"""
Numbers:
https://www.codewars.com/kata/search/python?beta=false&order_by=rank_id%20asc&q=&tags=Numbers



https://www.codewars.com/kata/50654ddff44f800200000004/train/python
https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python
https://www.codewars.com/kata/53ee5429ba190077850011d4/train/python
https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python

"""
