# Test 1. 
# We need to create a variable, 'x' (lowercase. You can assign this whatever you want.)
# Write your code below this line.

x = 1.5

# Write your code above this line.

print("Varibale: 'x', equals: ")
print(x)

# Test 2.
# We need to create a variable, 'y' (lowercase), this will be an integer.
# Write your code below this line.

y = 100

# Write your code above this line.

print("Variable: 'y' (integer), equals: ")
if isinstance(y, int):
    print(y)
else:
    print("Test #2 failed: 'y' is not an integer.")

# Test 3.
# We need to create a variable, 'z' (lowercase), this will be a string.
# Write your code below this line.

z = "Hello World!"

# Write your code above this line.

print("Variable: 'z' (string), equals: ")
if isinstance(z, str):
    print(z)
else:
    print("Test #3 failed: 'z' is not a string.")