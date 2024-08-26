# Welcome to Manu Python Day 2

"""
This statement is a comment
written in more than one line

"""

# print("Hello, World!")

# print("Hello, World Collins")

# PRINT FUNCTION
# print("  ") #In built command to print out a string or a number

# print("Manu Python Day 2")

# VARIABLES
# A variable is a container for storing data values.

# Students = "John Doe, Lynn Mwangi, Kennedy Muli"
# school = "UON, JKUAT, KU"
# numbers = 1, 2,3, 4, 5

# print("Hello World")
# print(Students)
# print(1,2,3,4,5)

### Types of Data

#string = anything other than a number ie letters. 

# Accessing the variable
#print(Students)
#print(Students, school, numbers) 


# Converting number to string 

#list = [1, 2, 3, 4, 5 ] # number
#list2 = ["1, 2, 3, 4, 5"] # string

# Python Operators
#Operators are used to perform operations on variables and values
"""
print(10 + 5) #addition
print(10 - 5) #subtraction
print(10 * 5) #multiplication
print(10 / 5) #division
print(10 % 3) #modulus
print(10 ** 3) #exponentiation

# Comparison Operators

#equals - gives either true or false
print(10 == 5) #equal
print(10 == 10) #equal
print(10 != 9) #not equal
print(10 > 9) #greater than
print(10 < 9) #less than

print(10 // 3) #flow division(removing decimals after the point)

"""

# In Python Index starts from 0

# Accessing values in strings

# Students = "John Doe, Lynn Mwangi, Kennedy Muli"

#print(Students) #Accessing the whole string
#print(Students[0]) #Accessing first(number in the brackets) character
#print(Students[0:5])


#Data Structures

# 1. Lists
# A list is a collection which is ordered and changeable. In Python lists are written in square brackets.
"""
Students = ["John Doe", "Lynne Mwangi", "Kennedy Muli"] #A list
Students = "John Doe, Lynne Mwangi, Kennedy Muli" #string

print(Students[0]) # Accessing first element in the list
print(Students[-1]) 

print(Students[1:3]) #Accessing the second and third element in a list

# Mutability and order in lists

Students = ["John Doe", "Lynne Mwangi", "Kennedy Muli", "Jeremiah Otieno"] #A list

print(Students[0]) = "Roy Kibet" #Changing the first element in a string

Students[0] = "Roy Kibet"

print(Students)

#Methods in list

Students.append("Roy Kibet") #Adding an element to the list
print(Students)
"""

# 2. Tuples
# A tuple is a collection which is ordered and unchangeable (immutable). In Python tuples are written with round brackets
"""
Area of a rectangle = length * width
location = longitude, latitude

rectangle = (10, 5) # Tuple
 print(rectangle[0])
"""


# 3. Sets

  


### Conditional Statements ###
## Control Flow

### 1. If Statement

# We take password input: Please re-enter your password

# condition1 check if the password has at least 8 characters
# condition2 check if the password has a number 
# condition3 check if the password has a special character

# Example1: Automatic Phone Balance Refill
"""
phone_balance = 4
bank_balance = 1000

if phone_balance < 20:
    phone_balance += 50
    bank_balance -= 50
    print("Your account balance is now: ", phone_balance)
    print("Your bank balance is now: ", bank_balance)
"""

# Example2: Automatic Phone Balance Refill
"""
phone_balance = 25
bank_balance = 1000

if phone_balance < 20:
    phone_balance += 50
    bank_balance -= 50
    print("Your account balance is now: ", phone_balance)
    print("Your bank balance is now: ", bank_balance)
"""

# No change occurs since the first statement is false. Therefore, Python doesn't execute code.

# Example3: Checking Grocery Budget
"""
grocery_budget = 50
cost_of_items = 45

if cost_of_items <= grocery_budget:
    grocery_budget -= cost_of_items
    print("Items purchased: Remaining budget is:", grocery_budget)
else: 
    print("Not enough budget: You need", cost_of_items - grocery_budget, "more.")
"""

# Example4: Checking Grocery Budget
"""
grocery_budget = 50
cost_of_items = 70

if cost_of_items <= grocery_budget:
    grocery_budget -= cost_of_items
    print("Items purchased: Remaining budget is:", grocery_budget)
else: 
    print("Not enough budget: You need", cost_of_items - grocery_budget, "more.")
"""


# Example5: Checking if a number is even or odd
"""
print( 10 % 2) # modulus(remainder after dividing)
# In modulus if a number is even, the result will be zero. 
"""

"""
number = 6

if number % 2 == 0: # == is called comparison operators
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")


name = input("Please enter your name: ")
number = input("Please enter your number: ")
number = int(number)

if number % 2 == 0:
    print("Hello " + name + "Your number: " + str(number) + " is even.")
else:
    print("Hello " + name + " Your number: " + str(number) + " is odd.")
    """

# Example6: Determining Weather Clothing
"""
#If the temperature is below 15 degrees Celsius, you should wear a coat.
temperature = 10 
coat_required = False

if temperature < 15:
    coat_required = True
    print("Is a coat required?", coat_required)
"""


# Example 7: Nested IF Statement(Having an if statement inside another if statement)
"""
x = 41
if x > 10:
 print("Above ten,")
 if x > 20:
    print("and also above 20!")
 else:
    print("but not above 20.")
"""

### Simple Program on Weather ###
"""
season = input('What season are we in? ')

if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')
"""


### Simple Calculator ###
"""
num1 = int(input("num1: "))
op = input("Operator: ")
num2 = int(input("num2: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")
"""
    


### 2. For loop (iterate), While loop

#FOR LOOP(definite iterations)
"""
students = ["John Doe", "Lynn Mwangi", "Kennedy Muli", "Jeremy Otieno"] # List

for student in students:
    print(student)

print("Finished printing students")
"""

# Components of a for loop
# 1. The iterable
# 2. The loop variable
# 3. The body of the loop


### Range Function
"""
# range(start, stop, step)

for i in range(1, 10, 2):
    print(i)
# Python will print starting from 1 to 10, and having intervals of two(step). 

for i in range(5):
    print("Welcome to today's class.")
# Using the same function, Python can print the sentence the number of times allocated in the brackets.
"""

### WHY LOOP
# Why loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition.
# Why loop has indefinite iterations. It only has conditions.
"""
i = 0
while i < 5:
    print(i)
    i += 1



f = open("students.txt","r")
print(f.read())

f = open("students.txt","r")
for x in f:
    print(x)
"""


### PYTHON MODULES ###
"""
A Python module can be defined as a python program file which contains a python code including python functions, class and variables.
In other words, we can say that our python code file saved with the extension (.py) is treated as the module.
We may have a runnable code inside the Python module.
Modules in Python provide us the flexibility to organize the code in a logical way.

Loading the module in our python code, we use:
1. The (import) statement
2. The (from-import) statement

# The Import Statement
It's used to import all the functionality of one module into another. 
Here, we must notice that we can use the functionality of any python source file by importing that file as the module into another python source file.
We can import multiple modules with a single import statement, but a module is loaded once regardless of the number of times, it has been imported into our file.

# The from-import Statement
Instead of importing the whole module into the namespace, python provides the flexibility to import only the specific attributes of a module.
This can be done by using (from < module-name> import <name 1>, <name 2>..., <name n>) statement.

# Renaming a module
You can create an alias when you import a module, by using the (as) keyword:
i.e import mymodule as mx

# Built-in models
There are several built-in modules in Python, which you can import whenever you like.

"""

### Reading and Writing to text files in Python
"""
File handling is an important part of any web applicayion.
Python has several functions for creating, reading, updating, and deleting files.

# The key function for working with files in Python is the open() function
The open() function takes two parameters; filename and mode.

The are four different methods(modes) for opening a file.
1. "r" - Read - Default value. Opens a file for reading, error if the file does not exist.
2. "a" - Append - Opens a file for appending, creates the file if it does not exist.
3. "w" - Write - Opens a file for writing, creates a file if it does not exist.
4. "x" - Create - Creates the specified file, returns an error if the file exists.

# Syntax
To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")

# Open a File on the Server
Assume we have the following file, located in the same folder as Python:

  demofile.txt
  Hello!
      This file is for testing purposes.
      Good Luck!
To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:

example
f = open("demofile.txt", "r")
print(f.read())

If the file is located in a different location, you will have to specify the file path:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

# Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many characters you want to return:
example: Return the 10 first characters of the file
f = open("demofile.txt", "r")
print(f.read(10))

By looping through the lines of the file, you can read the whole file, line by line:

#loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
print(f.read(10))

### Writing Files ###

Write to an existing file

To write to an existing file, you must add a parameter to the open() function.
1. "a" - Append - will append at the end of the file
2. "w" - Write - will overwrite any existing content

#Open the file "demofile2.txt" and append content to the file:

f = open("demofile2.txt", "a")
f.write("\nNow the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

### Delete a File ###
 
To delete a file, you must import the OS module, and run its os.remove() function:

import os
os.remove("demofile.txt")

### Delete a Folder ###
 
To delete an entire folder, use the os.rmdir() method:
- Remove the folder "myfolder"
- Note: You can only remove empty folders.

import os
os.rmdir("myfolder")

"""