# Simulate the binomial process
from numpy.random import binomial

# The prob of success of the experiment
p = 0.3
# The total number of experiments
n = 100

# run a single simulation
success = binomial(n, p)
print(f'Total success: {success}')

# calculate moments of a binomial distribution
from scipy.stats import binom
mean, var, _, _ = binom.stats(n, p, moments='mvsk')
print(f'Mean={mean:.3f}, Variance={var:.3f}')

# PMF for binomial distribution
dist = binom(n, p)
print('-----------PMF---------------')
for n in range(10, 110, 10):
    print(f'P of {n} successes: {dist.pmf(n) * 100:.3f}%')

# CDF for binomial distribution
dist = binom(n, p)
print('-----------CDF---------------')
for n in range(10, 110, 10):
    print(f'P of {n} successes: {dist.cdf(n) * 100:.3f}%')