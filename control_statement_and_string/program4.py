

print("""
Q)Write a program to search a number or a string in a list and print it. Read the number /string to be searched, from the user. Make use of for and if statements.

Ans)
""")

my_list = [5, 2, 'a', 'Karim', 10, '3']
print(my_list)
element = input("Enter what you want to search from the above list: ")
isNumber = False

try:
    int(element)
    isNumber = True
except:
    isNumber = False


found = False
for i in my_list:
    if isNumber and i == int(element):
        found = True
        break
    elif i == element:
        found = True
        break
if found:
    print("Found it!")
else:
    print("Not found!")
