

print("""
Q) Write a Python program to create Fibonacci series upto n using Lambda.

Solution:-
""")

n= int(input("Enter Fibonacci series length: "))

fib_list=[0,1]

any(map(lambda _:fib_list.append(sum(fib_list[-2:])), range(2,n)))

print("Fibonacci series: ",fib_list)