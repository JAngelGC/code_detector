# Define a function to calculate the sum of a number
def summation(n):
    if n == 0:
        return 0
    else:
        return n + summation(n - 1)

# Test the summation function
number = 5
print(f"The summation of {number} is:", summation(number))