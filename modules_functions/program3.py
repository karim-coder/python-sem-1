
print("""
Q) Write a Python program to sort a list of dictionaries using Lambda.

Solution:-
""")

list = [{"name": "Karim", "age": 25},
       {"name": "Nawroz", "age": 23},
       {"name": "Hussain", "age": 24}]


print("The list printed sorting by age: ")
print(sorted(list, key=lambda i: i['age']))