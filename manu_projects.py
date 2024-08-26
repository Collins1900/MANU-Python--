### Creating a Function

# A function is a block of code that only runs when it is called. 
# You can pass data, known as parameters, into a function. A function can return data as result.
"""
def my_function():
    print("Hello from a function")

my_function()
"""

### Arguments
# Information can be passed into functions as arguments. 
# Arguments are specified after the function name, inside the parentheses. 
# You can add as many arguments, just separate them with a comma.
"""
def my_function(fname):
    print(fname + " is a student at the University of Nairobi.")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
my_function("Albert")
"""

### Mathematical Function Example
# Let's define a mathematical function using a function. 
# We keep multiplying the base_num with pow_num(using a for loop)
"""
def raise_to_power(base_num, pow_num):
    results = 1 
    for index in range(pow_num):
        results *= base_num
    return results

raise_to_power(10, 2)
"""

# example
"""
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

# calling the function
cylinder_volume(10, 3)
# using user input
height = int(input(7)) 
radius = int(input(5))
print("The volume of your cylinder is :", cylinder_volume(height, radius))
"""

# Python Classes and Objects
""" Classes are used for:
  1. Creating custom data types
  2. Grouping related data and functions together
  3. Implementing more complex programming concepts like inheritance and encapsulation
"""
# Creating a Class
#To create a class, we use the keyword "class"
"""
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)
"""

# The init() Function
"""
To understand the meaning of classes, we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.

We use the __init__() function to assign values to object properties or other operations that are necessary when the object is being created:
"""
# example 1
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
p2 = Person("Jane", 42)
p3 = Person("Peter", 22)

print(p1.name)
print(p3.age)
"""

# example 2
"""
class Student:
    def __init__(self, gender, reg_no, year_of_study, faculty, gpa):
        self.gender = gender
        self.reg_no = reg_no
        self.year_of_study = year_of_study
        self.faculty = faculty
        self.gpa = gpa

john_Doe = Student("Male", "X32/345235/2022", 3, "Main Campus", 2.2)
jane_Doe = Student("Female", "F16/234234/2022", 5, "Kikuyu Campus", 3.5)

print(john_Doe.gpa)
print(jane_Doe.faculty)
"""


### Practice Projects ###

# Project 1. Multiple-Choice Quiz For Students 
"""
class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

username = input("Enter your name: ")
reg_no = input("Enter your Registration Number: ")
print("\nThanks " + username + ", Below is your quick test\nSelect the synonym of each of the following words:")

question_propmts = [
    "Vicissitude\n\t(a) sorrows\n\t(b) misfortunes\n\t(c) changes\n\t(d) surprises\n\n",
    "Epitome\n\t(a) Precise\n\t(b) Summary\n\t(c) Spurn\n\t(d) Exemplar\n\n",                                      
    "Imbecile\n\t(a) Sane\n\t(b) Astute\n\t(c) Foolish\n\t(d) Aid\n\n",                                      
    "Abeyance\n\t(a) Suspension\n\t(b) Persistence\n\t(c) Continuation\n\t(d) Rigid\n\n",                                    
    "Yokel\n\t(a) Intrigues\n\t(b) Simple-minded\n\t(c) Victorious\n\t(d) Noise\n\n",                                
]

quiz = [
    Questions(question_propmts[0], "c"),
    Questions(question_propmts[1], "d"),
    Questions(question_propmts[2], "c"),
    Questions(question_propmts[3], "a"),
    Questions(question_propmts[4], "b"),
]

def run_test(quiz):
    score = 0
    for question in quiz:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("At " + username + " You got " + str(score) + "/" + str(len(quiz)) + " correct in your test.")

run_test(quiz)
"""

# Project 2. Simple Calculator GUI
# This project creates a basic calculator using the tkinter library.
"""
import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to append characters to the entry
def append_to_entry(test):
    entry.insert(tk.END, test)

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for displaying the expression
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons and their layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), 
    # The '=' button should be here
    ('=', 4, 3),  # Make sure '=' is included in this position
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=evaluate_expression)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: append_to_entry(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Add a clear button
clear_button = tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)  # Moved to a separate row for clarity

# Run the main loop
root.mainloop()
"""

# Rroject 3. Guess the Number Game GUI
 
"""
import tkinter as tk
import random

# Function to check the guess
def check_guess():
    guess = int(entry.get())
    if guess < number:
        result_label.config(text="Too low! Try again.")
    elif guess > number:
        result_label.config(text="Too high! Try again.")
    else:
        result_label.config(text="Correct! You guessed the number")
        guess_button.config(state='disabled')

# Function to reset the game
def reset_game():
    global number
    number = random.randint(1, 100)
    result_label.config(text="Guess a number between 1 and 100")
    entry.delete(0, tk.END)
    guess_button.config(state='normal')

# Creat the main window
root = tk.Tk()
root.title("Guess the Number")

# Generate a random number
number = random.randint(1, 100)

# Create a label for instructions
instruction_label = tk.Label(root, text="Guess a number between 1 and 100", font=('Arial', 14))
instruction_label.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(root, font=('Arial', 14))
entry.pack(pady=10)

# Create a button to submit the guess
guess_button = tk.Button(root, text="Guess", font=('Arial', 14), command=check_guess)
guess_button.pack(pady=5)

# Create a label to display the result
result_label = tk.Label(root, text=" ", font=('Arial', 14))
result_label.pack(pady=10)

# Create a button to reset the game
reset_button = tk.Button(root, text="Reset Game", font=('Arial', 14), command=reset_game)
reset_button.pack(pady=10)

# Run the main loop
root.mainloop()
"""

# Project 4. Basic Analog Watch

import turtle
import datetime

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Simple Watch with Python Turtle")

# Create the turtle for drawing the clock face
clock = turtle.Turtle()
clock.penup()
clock.hideturtle()
clock.speed(0)

# Draw the clock face
def draw_clock_face():
    clock.goto(0, -250)
    clock.pendown()
    clock.circle(250)
    clock.penup()
    for hour in range(12):
        angle = (360 / 12) * hour
        clock.goto(0, 0)
        clock.setheading(-angle + 90)
        clock.penup()
        clock.forward(200)
        clock.pendown()
        clock.forward(50)
        clock.penup()
        clock.goto(0, 0)
        clock.setheading(-angle + 60)
        clock.forward(160)
        clock.write(str(hour + 1), align="center", font=("Arial", 24, "normal"))
        clock.penup()
        clock.goto(0, 0)

# Function to draw the hands of the watch
def draw_hand(length, angle, width):
    hand = turtle.Turtle()
    hand.shape("arrow")
    hand.shapesize(stretch_wid=width, stretch_len=length)
    hand.penup()
    hand.goto(0, 0)
    hand.setheading(angle)
    return hand

# Update the watch hands
def update_hands():
    now = datetime.datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    hour_angle = (360 / 12) * hour + (360 / 12) * (minute / 60)
    minute_angle = (360 / 60) * minute + (360 / 60) * (second / 60)
    second_angle = (360 / 60) * second

    hour_hand.setheading(90 - hour_angle)
    minute_hand.setheading(90 - minute_angle)
    second_hand.setheading(90 - second_angle)

    screen.update()
    screen.ontimer(update_hands, 1000)  # Update every second

# Draw the clock face and create hands
draw_clock_face()
hour_hand = draw_hand(100, 90, 1)
minute_hand = draw_hand(150, 90, 1)
second_hand = draw_hand(200, 90, 0.5)

# Update the hands every second
update_hands()

# Keep the window open
turtle.done()



# Project 5. Digital Watch
"""
import tkinter as tk
import time

# Function to update the time on the label
def update_time():
    current_time = time.strftime('%I:%M:%S %p') #Get the current time with seconds
    label.config(text=current_time) #Update the label with the current time
    label.after(1000, update_time) #Call this function again after 1 second

# Set up the main window
root = tk.Tk()
root.title("Digital Watch")

# Create a label to display the time
label = tk.Label(root, font=('calibri', 80, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

# Add some additional styling
label.config(padx=50, pady=50, relief='ridge', bd=10)

# Start updating the time
update_time()

# Keep the window open
root.mainloop()
"""



### QUICK TEST ###

# 1. Define a variable x and assign the value 25 to it. Write a Python expression to calculate the square of x and store it in a variable y.
x = 25
y = x ** 2

# What will be the output of the following code? Explain why. 
a = 5
b = 2.0
c = a // b
print(c)
#The result of this code will be 2. This is because the python operator divides and rounds down to the nearest integer(2)

# 2. Write a Python program that asks the user to enter a number. The program should check whether the number is positive, negative, or zero and print an appropriate message. 
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 3. Write a for loop that prints all even numbers between 1 and 20 (inclusive)
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Write a while loop that asks the user to input a number. The loop should continue to run until the user inputs the number 0.
number = -1 # initializing the variable to any value other than 0
while number != 0:
    number = int(input("Enter a number (0 to exit): "))

# 4. Define a function is_prime(n) that takes an integer n as input and returns True if n is a prime number, and False otherwise
def is_prime(n):
    """
    Returns True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 5. Create a list of all odd numbers between 10 and 30 using list comprehension.
odd_numbers = [n for n in range(10, 31) if n % 2 != 0]
print(odd_numbers)  # Output: [11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

# Appending the number 100 to the above list
odd_numbers.append(100)
print(odd_numbers)  # Output: [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 100]

### WEEK 2 PROJECT ###

# Defining the questions as tuples with the question, answer options, and correct answer
questions = [
    ("What is the capital city of Kenya?", ["A. Mogadishu", "B. Nairobi", "C. Cairo", "D. Kigali"], "B"),
    ("What is the largest country in the world?", ["A. Seychelles", "B. Canada", "C. Russia", "D. Japan"], "C"),
    ("Which city hosts the EAC Headquarters?", ["A. Kampala", "B. Mombasa", "C. Nakuru", "D. Arusha"], "D"),
    ("What is the smallest planet in our solar system?", ["A. Earth", "B. Mars", "C. Mercury", "D. Jupiter"], "C"),
    ("Which sport is Kenya known for at the Olympics?", ["A. Athletics", "B. Swimming", "C. Gymnastics", "D. Golf"], "A")
]

# Defining a function to ask a single question and return whether the answer is correct or not
def ask_question(question, options, answer):
    print("\n" + question)
    for option in options:
        print(option)
    user_answer = input("Enter your answer (A/B/C/D): ")
    if user_answer.upper() == answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

# Defining the main game function that asks all the questions, keeps score, and prints the final result
def quiz_game():
    print("Welcome to Collins' Python Project Quiz Game!")
    print("You will be asked 5 multiple-choice questions. Select an answer (A/B/C/D) for each question.")
    score = 0
    for question in questions:
        validated = False
        while not validated:
            validated = True
            score += ask_question(question[0], question[1], question[2])
            if score < 0 or score > len(questions):
                print("Error: Invalid score detected.")
                score = 0
                validated = False
    print(f"\nYou scored {score} out of {len(questions)}!")
    if score >= 3:
        print("Congratulations Champ! You won!")
    else:
        print("Sorry, you lost. Better luck next time.")

# Call the main game function to run the quiz
quiz_game()