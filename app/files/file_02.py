import random

# Define a list of colors
colors = ['red', 'green', 'blue', 'yellow', 'orange']

# Select a random color
selected_color = random.choice(colors)
print("Selected color:", selected_color)

# Define a dictionary of fruits and their prices
fruits = {'apple': 2.5, 'banana': 1.0, 'orange': 1.5, 'grape': 3.0}

# Select a random fruit
selected_fruit = random.choice(list(fruits.keys()))
print("Selected fruit:", selected_fruit)

# Define a function to calculate the square of a number
def square(x):
    return x ** 2

# Generate a random number
random_number = random.randint(1, 10)
print("Random number:", random_number)

# Calculate the square of the random number
squared_number = square(random_number)
print("Square of random number:", squared_number)