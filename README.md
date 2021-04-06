# CodeClub 2021 April

> 🚧 Under construction 🚧


## Basics

### Approach: 

- minimalistic (no external tools other than Python and a text editor)
- focusing on the basics

### Topics

- Python fundamentals
- perhaps later look into web development, if there is interest for it

### Course content

**Main** course content will be here on Github.

**Additional** course content will be include articles, blog posts, videos and tutorials. 


- [RealPython articles](https://realpython.com/python-data-types/)
- [Codewars exercises](https://www.codewars.com/kata/search/python?q=&r[]=-8&beta=false)
- [Python for you and me](http://pymbook.readthedocs.io/en/latest/#)
- [The Hitchhiker’s Guide to Python!](http://docs.python-guide.org/en/latest/)
- [Learn Python the Hard Way](https://learnpythonthehardway.org/book/)
- [Python on Codeacademy](https://www.codecademy.com/learn/python)
- [Python foundations](https://courses.spatialthoughts.com/python-foundation.html#hello-world)


### Lesson 1

- What is Python used for
- code, whitespace, comments
- data types
- variables
- operators (+, -, *, **, /, //, and, or, not)
- comparison of variables (==)
- functions (definition, parameters, function calls, return values)
- built-in functions

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


## Lesson 2

- Flow control: if/else
- Loops: for, while
  - breaking out of loops
- TBD

RECAP - What have we learned on the first session

## Whitespace

- Whitepsace is meainingful
- Whitespace is used for "indentation"
- Spaces and tabs (you can use either one, just be consistent - it's best to use four spaces)

## Comments

- Comments are not executed by the interpreter
- Comments are written after the # symbol, or betweenn triple quotes (especially mulit-line comments)

## Data types 

### We had a look at a few types of data:

- `int`
    "whole numbers"
    Example: 1, 7, 42
- `float`
    numbers with decimal point
    Example:  0.2, 5.0, 21972.129871
- `boolean`
    Values representing "Boolean logic": True/False. 
    True and False are the only boolean values.
- `str` (string)
    Textual data types. They are between single or double quotes/
    Example: "padlizsankrém", 'spagetti', 'rántott hús'
    Multi-line strings can be defined between triple quotes.
    
(We will look at other types of data a bit later.)

### The type() built-in function

You can check the data type of a value using the built-in "type" function:
- `type('pizza')` will tell you that 'pizza' is a string, 
- `type(1.0)` will tell you that 1.0 is a float.


## Variables

Varialbes hold some kind of data. 
To define a variable, you just have to type the name of the variable, and equality sign, and the value of it:

`my_favourite_food = 'anything except coriander!'`

The equality sign here stands for the "assignment" - we assign the string 'anything except coriander!' to the variable my_favourite_food

Variables are used to store data in your program, so that you can re-use them later.

## Functions

We can write functions to make our code re-usable. For example, we might want to reuse a function that calculates some value based on some input.

We use the def keyword to define a function.





