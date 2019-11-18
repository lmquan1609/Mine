# Sampling a normal distribution
import numpy as np

# define the distribution
mu, sigma = 50, 5
n = 10

# generate the sample data
sample = np.random.normal(mu, sigma, n)
print(sample)

# Plot the normal distribution
from scipy.stats import norm
import matplotlib.pyplot as plt

# define the distribution
mu, sigma = 50, 5
n = 10

# Create distribution
dist = norm(mu, sigma)
# plot pdf
values = [value for value in range(30, 70)]
probs = [dist.pdf(value) for value in values]
plt.plot(values, probs)
plt.show()

# plot cdf
cprobs = [dist.cdf(value) for value in values]
plt.plot(values, cprobs)
plt.show()

# calculate the values that define the middle 95%
from scipy.stats import norm

# define the distribution
mu, sigma = 50, 5

# Create distribution
dist = norm(mu, sigma)
low_end, high_end = dist.ppf(0.025), dist.ppf(0.975)
print(f'Middle 95% between {low_end:.2f} and {high_end:.2f}')