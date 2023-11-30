import random

# Generate 300 random numbers
random_numbers = [random.uniform(0, 1) for _ in range(300)]

# Format numbers as strings
formatted_numbers = [f"{num:.18e}" for num in random_numbers]

# Save numbers to a file
with open("NewSample.txt", "w") as file:
    for num in formatted_numbers:
        file.write(num + "\n")

print("Random numbers have been generated and saved to 'random_numbers.txt'.")
