#1. Write a Python program to accept two integers and check whether they are equal or not.
#Test Data : 15 15
num1 = int(input("Enter the first integer :"))
num2 = int(input("Enter the second integer :"))

if (num1 == num2):
    print("num1 and num2 are equal")

else:
    print("num1 and num2 are not equal")

#2. Write a Python program to check whether a given number is even or odd.
#Test Data : 15

num = int(input("Enter the number :"))
if(num%2 == 0):
    print(f" {num} is even integer " )
else:
    print(f"{num} is odd integer")

#3. Write a python program to check whether a given number is positive or negative.
#Test Data : 15    

n = int(input("Enter the number :"))
if (n>0):
  print(f"{n} is positive")
else:
  print(f"{num} is negative")


# 4. Write a python program to find whether a given year is a leap year or not.
#Test Data : 2016  
year = int(input(" Enter the Year :"))
if (year%4==0 and year%100!=0) or year%400 ==0 :
  print(f"{year} is a leap year")
else:
  print(f"{year} isn't year")

#5. Write a python program to read the age of a candidate and determine whether he is eligible to cast his/her own vote.
#Test Data : 21
age = int(input("Enter your age: "))
name = input(" Enter the Name : ")

if age >= 18:
    print(f"{name} has eligible to cast your vote.")
else:
    print(if"{name} has not eligible to cast your vote yet.")

#6. Write a python program to find the largest of three numbers.
#Test Data : 12 25 52
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the largest number
print("The largest number is:", largest)    
    
#7.Write a C\python program to read the roll no, name and marks of three subjects and calculate the total, percentage and division.
#Test Data :
#Input the Roll Number of the student :784
#Input the Name of the Student :James
#Input the marks of Physics, Chemistry and Computer Application : 70 80 90
#Expected Output :
#Roll No : 784
#Name of Student : James
#Marks in Physics : 70
#Marks in Chemistry : 80
#Marks in Computer Application : 90
#Total Marks = 240
#Percentage = 80.00
#Division = First

roll_no = input("Input the Roll Number of the student: ")
name = input("Input the Name of the Student: ")
physics_marks = int(input("Enther the Physics mark :"))
chemistry_marks = int(input("Enther the Chemistry marks :"))
comp_app_marks = int(input("Enther the Computer Application  marks :"))

# Calculate the total marks
total_marks = physics_marks + chemistry_marks + comp_app_marks

# Calculate the percentage
percentage = (total_marks / 300) * 100

# Determine the division
if percentage >= 60:
    division = "First"
elif percentage >= 50:
    division = "Second"
elif percentage >= 40:
    division = "Third"
else:
    division = "Fail"

# Print the student's details and results
print("Roll No:", roll_no)
print("Name of Student:", name)
print("Marks in Physics:", physics_marks)
print("Marks in Chemistry:", chemistry_marks)
print("Marks in Computer Application:", comp_app_marks)
print("Total Marks =", total_marks)
print("Percentage =", "%.2f" % percentage)
print("Division =", division)

#8.Write a PYTHON program to read temperature in centigrade and display a suitable message according to the temperature state below:
#Temp < 0 then Freezing weather
#Temp 0-10 then Very Cold weather
#Temp 10-20 then Cold weather
#Temp 20-30 then Normal in Temp
#Temp 30-40 then Its Hot
#Temp >=40 then Its Very Hot
#Test Data :
#42
 temperature = float(input("Enter the temperature in Celsius: "))

# Determine the temperature state and display a suitable message
if temperature < 0:
    print("Freezing weather")
elif 0 <= temperature <= 10:
    print("Very Cold weather")
elif 10 <= temperature <= 20:
    print("Cold weather")
elif 20 <= temperature <= 30:
    print("Normal in Temp")
elif 30 <= temperature <= 40:
    print("Hot")
else:
    print("Very Hot")

#9.Write a C program to check whether a character is an alphabet, digit or special character.
#Test Data :
#@
character = input("Enter a character: ")

# Check the type of the character
if character.isalpha():
    print("The character is an alphabet.")
elif character.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")
#10.Write a python program to calculate profit and loss on a transaction.
#Test Data :
#500 700
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

# Calculate the profit/loss
profit = selling_price - cost_price

# Check if it's a profit or loss
if profit > 0:
    print("Profit:", profit)
elif profit < 0:
    print("Loss:", profit)
else:
    print("No profit or loss.")    



    
