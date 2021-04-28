# Python cheatsheet

Table of contents

<!-- toc -->

- [Whitespace](#whitespace)
- [Comments](#comments)
- [Variables](#variables)
- [Data types](#data-types)
- [Functions](#functions)
- [Loops](#loops)

<!-- tocstop -->

## Whitespace

For Python, **whitespaces** (spaces and tabs) in our code are significant.  
They are used to declare a "code block" - for example, the code of a function body is separated from the outer code by one level of **indentation**.

```
def find_meaning_of_life():
    return 42
```

As another example, the bodies of `if/else` statements are also indented by one level:

```
favourite_food = 'beer'

my_fridge = ['beer', 'pizza']

if favourite_food in my_fridge:
    print('Yaay!')
else:
    print('Sad! :(')
```

For whitespace, you can use either **spaces** or **tabs** (but not both).

## Comments

```
# Lines starting with # are comments
# These are not evaluated by Python, they are completely ignored, 
# So we can use this to document our code for others
```

## Variables

We declare variables by assigning a **value** to a **name**:  
We do this to be able to **re-use** these values in our code, and so we don't have to repeat ourselves.

```
favourite_food = 'mac and cheese'
```

In the above example, we have assigned the value `mac and cheese` to the name `favourite_food`.


A variable can be of any data type. In the above example, the `favourite_food` variable is a string. In the following example, we assing an integer type to the variable named `meaning_of_life`:  

```
meaning_of_life = 42
```


## Data types

### The type() built-in function

You can check the data type of a value using the built-in "type" function:
- type('pizza') will tell you that 'pizza' is a string, 
- type(1.0) will tell you that 1.0 is a float.

### Numeric types

- integers: `1, 2, 42`  
- floats: `3.0, 1.232, .01`

(There is a data type for complex numbers, but their usage is very rare)

#### Common operations 

We can use the common mathematical operations on numbers: `+`, `-`, `*`, `**` (exponent), `/`, `//`, `%` (modulo)

> Note: when you see the `>>>` sign, it refers to the interactive interpreter of Python: it's the "prompt" of Python. This is what you see when you start up Python on your computer.

```
>>> 5 * 5
25
```

```
>>> 3 ** 3
27
```

```
>>> 15 / 4
3.75
```

The `//` operator does "floor division":

```
>>> 15 // 4
3
```

The modulo (`%`) gives you the **remainder** of a division:

```
>>> 15 % 4
3
```

```
>>> IBM_stock_price_yesterday = 126
>>> IBM_stock_price_today = 127
>>> stock_price_change = IBM_stock_price_today - IBM_stock_price_yesterday
>>> stock_price_change
1
```


### Strings


Strings represent **text**. They are between single or double quotes.

```
food = 'spaghetti'
```

[Python docs](https://docs.python.org/3/tutorial/introduction.html?fbclid=IwAR3knUj3nO0-f2fYMS5Yb5MbGplB93buRymiE_07F06rufql14v5bKrzErk#strings)


#### Common operations


You can get the length of a string using the built-in `len` function:

```
>>> len('pizza')
5
```

We can make strings uppercase, lowercase, capitalized:

```
>>> 'broccoli'.upper()
'BROCCOLI'
>>> 'BEER'.lower()
'beer`
>>> 'joe'.capitalize()
'Joe'
```

(You might have noticed that we do this by appending a period (`.`) and then calling a function - these are called "methods" and we'll learn about them a bit later)

Strings can be added together

```
>>> 'I love ' + 'pizza'
'I love pizza'
```

We can check if a string starts with or ends with a particular prefix or suffix:

```
>>> 'tomato soup'.startswith('tomato')
True
```


You can count the number of times a string occurs in another string:

```
>>> foods = 'broccoli sausage pizza pizza hamburger spinach potatoes fris pizza pizza'
>>> foods.count('pizza')
4
```

You can "slice" them - this means that you can get a "substring" of them. For example, to get the first eight characters of the string from above, you could do:

```
>>> foods[0:8]
'broccoli'
```

You can do a lot with slicing. Check out this article: https://realpython.com/python-strings/#string-slicing


The full list of string methods can be seen [here in the official Python docs](https://docs.python.org/3/library/stdtypes.html#string-methods).


### Booleans

Values representing "Boolean logic": True/False. 

`True` and `False` are the only boolean values.

This is a [good article about booleans](https://thomas-cokelaer.info/tutorials/python/boolean.html?fbclid=IwAR0mg4nzR6uQ4JvneWMGzLH6yiYzeb4Lo_C83ddo5vwXAcy_-lRdH61Q-Gw#notes-about-booleans-and-logical-operators).


#### Common operations

Common boolean operators are the following logical operators: `and`, `or` and `not`.

`and` returns `True` if both sides are true. Otherwise, it returns `False`.

```
>>> True and True
True
>>> True and False
False
```

`or` returns True if any of the two sides is True:

```
>>> True or False
True
>>> False or False
False
```

`not` returns the opposite boolean value:

```
>>> not True
False
>>> not False
True
```

### Lists

Lists are used to group together values. 

```
squares = [1, 4, 9, 16, 25]
```

You can put any data type into a list.

[Python docs](https://docs.python.org/3/tutorial/introduction.html?fbclid=IwAR3knUj3nO0-f2fYMS5Yb5MbGplB93buRymiE_07F06rufql14v5bKrzErk#lists)

#### Common operations

Lists are very versatile, you can do a lot of things with them.

You can **slice** them, just like strings:

```
>>> my_list = [1, 2, 3]
>>> my_list[1:3]
[2, 3]
```

The third argument of the slice operator makes it possible to **skip items**, or to move through the list **backwards**:

```
>>> my_list = [1, 2, 3]
>>> my_list[0:3:2]
[1, 3]
```

You can use `my_list[::-1]` to traverse the list backwards `[::-1]` is a shorthand for "_from the beginning, to the end, in steps of minus one_":

```
>>> my_list = [1, 2, 3]
>>> my_list[::-1]
[3, 2, 1]
```


You can **index** them:

```
>>> my_list = [1, 2, 3]
>>> my_list[0]
1
```

You add an item to a list with the `append()` method:

```
>>> my_list = [1, 2, 3]
>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]
```

You can remove an item with the `remove()` method, and you can do a lot of other things - check out these articles for more:

- [RealPython](https://realpython.com/python-lists-tuples/#python-lists)
- [More on lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)


### Dictionaries

Official [Python docs here](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).

This is an empty dictionary:

```
stock_prices = {}
```

We can add some values to the dictionary like so:

```
stock_prices['IBM'] = 126
stock_prices['TSLA'] = 660
```

We can declare a dictionary like this as well:

```
stock_prices = {'IBM': 126, 'TSLA': 660}
```

Or we can do a dictionary for cocktail recipes - notice that the values are lists in this case:

```
cocktails = {}
cocktails['rob roy'] = ['whisky', 'angostura bitters', 'sweet vermouth', 'ice']
cocktails['old fashioned'] = ['whisky', 'angostura bitters', 'sugar', 'water', 'lemon peel', 'ice']
```

We can delete a dictionary key with the `del` keyword:

```
del cocktails['old fashioned']
```


Dictionaries are iterable objects - we can iterate over them.
To iterate over keys:

```
for cocktail in cocktails:
    print(cocktail)
```

To iterate over values:

```
for cocktail in cocktails.values():
    print(cocktail)
```

To iterate over both the keys and values, we can use the items() method on the dictionary:

```
for key, value in cocktails.items():
    print(key, value)
```

We can use the "in" operator on dictionaries:

```
>>> 'rob roy' in cocktails
True
```

Dicionaries are also called "look up tables" because we can look up things in them:

```
>>> cocktails['rob roy']
['whisky', 'angostura bitters', 'sweet vermouth', 'ice']
```

What happens if we try to look up a value that is not in the dictionary?

```
>>> cocktails['martini']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'martini'
```

We got a `KeyError`. This happens when we try to access a non-existent key in a dictionary.

Sometimes we want to look up a key in a dictionary but we're not sure if it's in it. 
We could check first if the key is in:

```
if 'martini' in cocktails:
    print(cocktails['martini'])
else:
    print('No recipe for martini')
```

Or we can use the `.get()` method on the dictionary:

```
cocktails.get('martini')
```

The above line will evaluate to `None`, because 'martini' is not stored in the dict.
`.get()` can take an optional default value, like so:

`dictionary.get("key im looking for", 'default_value')`  - if `'key im looking for'` is not in the `dictionary`, this expression will evaluate to `'default_value'`




### Sets

```
# A set is an unordered collection with no duplicate elements.
# it can be used to de-duplicate a list:

shopping_list = ['carrots', 'potatoes', 'cognac', 'olive oil', 'tonic water', 'beans', 'lentils', 'potatoes'] 

set(shopping_list)

# suppose there are two shopping lists,
# and you want to merge them and avoid duplications

shopping_list_1 = ['carrots', 'potatoes', 'cognac', 'olive oil', 'tonic water', 'beans', 'lentils', 'potatoes'] 
shopping_list_2 = ['potatoes', 'bread', 'eggplant', 'cognac', 'olive oil', 'tonic water', 'beans', 'lentils', 'potatoes'] 

# make them into sets (cast them with set()) 
set_1 = set(shopping_list_1)
set_2 = set(shopping_list_2)

# what is their union?
set_1.union(set_2)

# what is the intersection?
set_1.intersection(set_2)

# what is their difference? 
set_2.difference(set_1)
set_1.difference(set_2)
```

## Functions

We write functions to be able to **re-use** our code. If we have defined a function, we can use it later any time we want, for as many times as we want.

A function **definition** can look like the following:

```
def multiply(x, y):
    return x * y
```

A more complicated function might contain multiple lines, `if`/`else` statements, and any other code:

```
def multiply(x, y):
    if type(x) not in [int, float] or type(y) not in [int, float]:
        print("Not a number, cannot multiply!")
        return
    else:
        return x * y

```

A function **call** actually executes the function:

```
>>> multiply(5, 3)
15

>>> multiply(5, 'pizza')
'Not a number, cannot multiply!'
```

Some imporant points:

- The definition must start with the `def` keyword
- After the `def` keyword, we have to give a **name** to our function. The name should be in English, describing what the function does. The name has to be in `snake_case`, eg.: `multiply_by_two`
- After the name, there must to be an opening parenthesis ( `(` character), after which, there can be zero or more **arguments**, then a closing parenthesis (`)`), then a colon (`:`) character. 
- The function body is **indented** by one level - this is where we put the logic of the function
- Usually a function has a **return value** which is denoted by the `return` statement. However, it's not obligatory to have a return value - a function can just return nothing, or print something, or modify something (we will look at examples for each of these later).

Arguments can be considered as the "input" to your function - you get some data in the arguments, you do something with them in the function body, and you return something.


A very detailed article about functions can be read [here](https://realpython.com/defining-your-own-python-function/#functions-in-python). 

Funcions can have **positional arguments** and/or **keyword arugments**.

Positional arguments are **required** arguments - you have to pass them when you call the function. The **order is important**.
Keyword arguments are **optional** arguments - you can, but don't have pass them to the function when you call it. If you don't pass them, their **default** value will be used. Their order is not important.

[See this section in the above article](https://realpython.com/defining-your-own-python-function/#argument-passing)





## Loops

### For loop

`for` loops are used to **iterate over a sequence of values**.

For example, if we have a list, we can go over the items of the list, and print them, one by one.


```
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
```

Like variables and functions, loops can be use to **re-use our code**: we can repeat the same action a number of times. In the example above, we repeat the `print` function for all elements in the list.


```
# print the foods that are not 'broccoli'

foods = ['steak', 'broccoli', 'sausage', 'pizza', 'beer', 'spaghetti']

for food in foods:
    if food != 'broccoli':
        print(food) 
```


## Working with files

Opening a file is done with the `open` function:

`freq_words_file = open('hungarian.txt', 'r')`

You can **iterate** over the lines of a file:

```
common_words = []

for word in freq_words_file:
    common_words.append(word.strip())

# we have to close the file after we are done with it
freq_words_file.close()
```



Another example:

A better way of opening a file is using the `with` keyword - this way, we don't have to close it, as it will be closed automatically:

```
common_words = []

with open('hungarian.txt', 'r') as freq_words_file:
    for word in freq_words_file:
        common_words.append(word.strip())
```






