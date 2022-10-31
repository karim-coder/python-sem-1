
print("""
Q) Write a Python program to square and cube every number in a given list of integers using Lambda.

Solution:-
""")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
square_nums = list(map(lambda x: x ** 2, nums))
print("\nSquare every number of the said list: ",square_nums)
cube_numbs = list(map(lambda x:x**3, nums))
print("\nCube every number of the said list: ", cube_numbs)
