# import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Q1: Using NumPy create an array of random numbers between 0 and 1. The shape of the array must be (3, 4). Use seed to ensure that the results are reproducible. Create random numbers between 0 and 1 and set seed so the random output is reproducible
rng = np.random.default_rng(seed = 22)

# Set shape of array and fill with random output
rng.random(size = (3, 4))

# Q2: Create an array of random integers between 0 and 10. The shape of the array must be (3, 4). Create an array of random numbers and set a seed value so it is reproducible
rng = np.random.default_rng(seed = 23)

# Set upper and lower limits and size guidelines
arr = rng.integers(low = 0, high = 10, size = (3, 4))
arr

# Q3: Using NumPy, generate an array of 1000 random numbers from a standard normal distribution with a mean of 0 and a variance of 1. Create a histrogram with this array. Use the seed parameter to ensure the results are reproducible.
# Set parameters
mean = 0
variance = 1
std_dev = np.sqrt(variance)

# Make a random number generator
rng = np.random.default_rng(seed=12)

# Set random generator to an array with requirements. 
x = rng.normal(loc=mean, scale=std_dev, size=1000)

# Plot histogram
plt.figure(figsize=(10, 8))
plt.hist(x, bins = 20)
plt.title('Histogram', fontsize = 22)
plt.xlabel('Values from Random Number Generator')
plt.ylabel('Frequency')
plt.show()

# Q4: `arr = ["Orange", "Apple", "Pear"]` Using random.choice() from NumPy, generate an array from the list. The shape of the array must be (3, 4).
# Define array
fruit = np.array(["Orange", "Apple", "Pear"])

# Use random choice to determine order of fruit in array and define size 
arr = np.random.choice(fruit, size = (3, 4))
arr 
