# operators
"""
Python is a high-level, interpreted programming language that is widely used for web development, data science,
machine learning, and many other applications.
Here are some in-depth concepts that are important to understand when working with Python:

1. Data types: Python supports several built-in data types, including integers, floating-point numbers,
strings, Boolean values, and lists. Understanding how to work with these data types is essential for writing
Python programs.

2. Control flow statements: Python uses control flow statements such as if-else statements, loops, and
functions to control the execution of code. Understanding how to use these statements is key to writing
efficient and effective Python programs.

3. Functions: Functions are blocks of code that can be called multiple times within a program. Python
supports both built-in and user-defined functions, which can take arguments and return values.

4. Object-oriented programming (OOP): Python is an object-oriented programming language, which means
that it supports the creation of objects and classes. OOP concepts such as inheritance, encapsulation,
 and polymorphism are important to understand when working with Python.

5. Libraries and frameworks: Python has a vast ecosystem of libraries and frameworks that can be used
 to extend its functionality. Popular libraries and frameworks for Python include NumPy, Pandas,
 Django, Flask, and TensorFlow.

6. File I/O: Python supports reading from and writing to files on a local or remote system. Understanding
 how to read and write data to files is important for working with data in Python.

7. Exception handling: Exception handling is a technique for handling errors and unexpected events in a
program. Python supports exception handling through try-except statements.

8. Regular expressions: Regular expressions are patterns that can be used to search for and manipulate
text data in Python. Understanding regular expressions is important for working with text data in Python.

"""


# types_of_operators
"""

Python supports several built-in data types, including:

1)Integers: Integers are whole numbers that can be positive, negative, or zero. In Python, integers are 
represented by the int data type. Here are some examples:

x = 10
y = -5
z = 0

2)Floating-point numbers: Floating-point numbers are numbers with decimal points. In Python, floating-point
numbers are represented by the float data type. Here are some examples:

x = 3.14
y = -2.5
z = 0.0

3)Strings: Strings are sequences of characters. In Python, strings are represented by the str data type. 
Here are some examples:

x = "Hello, world!"
y = 'Python is awesome'
z = "I'm learning Python"

4)Booleans: Booleans are values that can be either True or False. In Python, Booleans are represented by 
the bool data type. Here are some examples:

x = True
y = False

A)Lists: Lists are ordered collections of values. In Python, lists are represented by the list data type. 
Here are some examples:

x = [1, 2, 3, 4, 5]
y = ["apple", "banana", "cherry"]
z = [1, "apple", True]

B)Tuples: Tuples are similar to lists, but they are immutable, which means they cannot be modified once 
they are created. 
In Python, tuples are represented by the tuple data type. Here are some examples:

x = (1, 2, 3, 4, 5)
y = ("apple", "banana", "cherry")
z = (1, "apple", True)

C)Sets: Sets are unordered collections of unique values. In Python, sets are represented by the set data
type. Here are some examples:

x = {1, 2, 3, 4, 5}
y = {"apple", "banana", "cherry"}
z = {1, "apple", True}

D)Dictionaries: Dictionaries are unordered collections of key-value pairs. In Python, dictionaries are 
represented by the dict data type. Here are some examples:

x = {"name": "John", "age": 30, "city": "New York"}
y = {"fruit": "apple", "color": "red"}
z = {1: "apple", 2: "banana", 3: "cherry"}

These are some of the most commonly used data types in Python.
"""

# Control flow statements
"""
Control flow statements are the statements that allow you to control the flow of execution of a Python 
program. In other words, they enable you to determine which code should be executed and 
when, based on certain conditions.

There are three main types of control flow statements in Python:

Conditional statements: Conditional statements are used to execute a block of code only if a certain 
condition is met. 
The most commonly used conditional statement in Python is the if statement. Here is an example:

x = 5
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")

In this example, the if statement checks if the value of x is greater than 0. If it is, then the 
statement print("x is positive") is executed. Otherwise, the statement print("x is non-positive") 
is executed.

Loop statements: Loop statements are used to execute a block of code repeatedly. The two most commonly 
used loop statements in Python are the for loop and the while loop. Here are some examples:

# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1

In the first example, the for loop is used to iterate over a list of fruits and print each fruit. 
In the second example, the while loop is used to print the numbers 1 through 5.

Function calls: Function calls are used to execute a specific function in a program. Functions are a 
key part of Python programming and can be used to organize code and make it more reusable. Here is an example:

def greet(name):
    print("Hello, " + name + "!")
    
greet("Alice")

In this example, the greet function is defined to take a single parameter name and print a greeting message. 
The function is then called with the argument "Alice", which causes it to print the message "Hello, Alice!".

These are the basic control flow statements in Python. They allow you to write programs that can make decisions, 
repeat tasks, and organize code using functions.
"""

# Functions
"""
Functions are a fundamental concept in Python programming. They allow you to write reusable blocks of code 
that can be called from other parts of your program. In this answer, we'll go over the basics of creating 
and using functions in Python.

Defining a Function
To define a function in Python, you use the def keyword followed by the name of the function, a set 
of parentheses that can contain one or more parameters, and a colon. The body of the function is indented 
and contains the code that the function executes.

Here's an example of a simple function that takes no parameters and prints a message:

def say_hello():
    print("Hello, world!")
In this example, the function is named say_hello. It doesn't take any parameters and simply prints the 
message "Hello, world!" when called.

Calling a Function
To call a function in Python, you simply use the name of the function followed by a set of parentheses 
that can contain any arguments that the function takes.

Here's how you would call the say_hello function defined in the previous example:

say_hello()
When you call a function, the code in the function's body is executed.

Parameters and Arguments
Functions can take one or more parameters, which are essentially variables that the function expects to 
receive when it is called. You specify the parameters in the function definition, inside the parentheses.

Here's an example of a function that takes two parameters and prints their sum:

def add_numbers(x, y):
    print(x + y)
In this example, the function is named add_numbers and takes two parameters, x and y. When the function 
is called with two arguments, the values of x and y are set to those arguments, and the function prints their sum.

add_numbers(3, 4)  # Output: 7
Return Values
Functions can also return a value, which is a way to pass data back to the code that called the function. To return 
a value from a function, you use the return keyword followed by the value you want to return.

Here's an example of a function that takes two parameters and returns their sum:

def add_numbers(x, y):
    return x + y
In this example, the function is named add_numbers and takes two parameters, x and y. When the function is called 
with two arguments, the values of x and y are set to those arguments, and the function returns their sum.

result = add_numbers(3, 4)
print(result)  # Output: 7
Default Parameter Values
You can also specify default values for parameters in a function definition. This allows you to call the function 
with fewer arguments, using the default values for any parameters that are not specified.

Here's an example of a function that takes two parameters, one of which has a default value:

def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")
In this example, the function is named greet and takes two parameters, name and greeting. The greeting parameter 
has a default value of "Hello". If you call the function with only one argument, the default value is used for 
the greeting parameter:

greet("Alice")  # Output: Hello, Alice!
If you call the function with two arguments, the second argument is used as the value for the greeting parameter:

greet("Bob",
"""

