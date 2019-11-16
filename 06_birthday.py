# example of the birthday problem max group size
n = 30
# number of days in the year
days = 365
# calculate prob for different group sizes
p = 1.0
for i in range(1, n):
    p *= (days - i)/days
    print(f'n = {i + 1}, prob = {(1 - p) * 100}%, invert prob: {p * 100}%')