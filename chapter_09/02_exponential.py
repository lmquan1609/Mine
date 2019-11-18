# Sampling a normal distribution
import numpy as np

# define the distribution
beta, n = 50, 10

# generate the sample data
sample = np.random.exponential(beta, n)
print(sample)

# Plot the exponential distribution
from scipy.stats import expon
import matplotlib.pyplot as plt

# define the distribution
beta = 50

# Create distribution
dist = expon(beta)
# plot pdf
values = [value for value in range(50, 70)]
probs = [dist.pdf(value) for value in values]
plt.plot(values, probs)
plt.show()

# plot cdf
cprobs = [dist.cdf(value) for value in values]
plt.plot(values, cprobs)
plt.show()