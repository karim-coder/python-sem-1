
print("""
Q) Write a program to print the addition of first 30 natural numbers. (Use while statement).

Ans)
""")
n = 30
i = 1
sum = 0
while(i <= n):
    sum += i
    i += 1
print("Addition of first %s natural numbers is: " % n, sum)
