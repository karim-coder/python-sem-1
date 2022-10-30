
print("""
Q) Write a Python program to determine whether a given year is a leap year.

Solution:-
""")

year = int(input("Enter year to check is lear year or not: "))

if(year % 400 ==0 ) or (year%100!=0) and (year%4 ==0):
  print("Given year is a leap year.") 
else:
   print("Given year is not a leap year.") 