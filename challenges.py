########################
#!/usr/bin/python
########################

# Challenge 1

#Write a program to check if a number is divisible by 5 or 7
 
number = int(input("enter number"))
if(number%7==0)and(number%5==0):
 print(f"The number{number} is divisible by both 5 or 7")
else:
    print(f"The number{number} is not divisible by 5 or 7")

# Challenge 2

#name = input("Enter your name")
#print(f"Your name is {John}")

# Challenge 3

num = 20
num += num
print(num)

# Challenge 4

prompt = "Enter your name so we can customize"
prompt += "In enter your name"
print(input(prompt))


# Dictionaries 
mary_fav_food = ['ugali','meat','vegetables']
jane_fav_food = ['rice','beef','juice']
fav_food = {'mary':mary_fav_food,'jane':jane_fav_food}
print(fav_food)