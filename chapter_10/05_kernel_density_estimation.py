import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity

# generate a sample
sample_1 = np.random.normal(20, 5, 300)
sample_2 = np.random.normal(40, 5, 700)
sample = np.hstack([sample_1, sample_2])

# plot the histogram
plt.hist(sample, bins=50)
plt.show()

# fit density
model = KernelDensity(bandwidth=2.0, kernel='gaussian')
sample = np.expand_dims(sample, 1)
model.fit(sample)

# sample probs for a range of outcomes
values = np.asarray([value for value in range(1, 60)])
values = np.expand_dims(values, 1)
probs = model.score_samples(values)
probs = np.exp(probs)

# plot the histogram and pdf
plt.hist(sample, bins=50, density=True)
plt.plot(values[:], probs)
plt.show()