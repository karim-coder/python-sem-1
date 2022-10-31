import math

print("""
Q) Write a program to read three numbers from user and compare the greatest and smallest of those numbers and print the appropriate message.

Ans)
""")


n = 3
min = math.inf
max = -math.inf
print("Enter three numbers")

for i in range(n):
    number = int(input(f"Enter number {i+1} : "))
    if(max < number):
        max = number
    elif(min > number):
        min = number

print("The largest number is: ", max)
print("The smallest number is: ", min)
