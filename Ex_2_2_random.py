"""(a) Generate a list of 100 random integers between 1 and 100. Calculate the mean,
median, and mode of that list.
(b) Store the number of times each integer appears in a dictionary.
(c) Assign each integer into one of ten groups, representing equal width bins [1, 10],
[11, 20], . . . , [91, 100]. Continue generating random integers until at least two
groups contain the same number of integers."""

import random, math
import numpy as np
# from scipy import stats

# Mode function
def mode_fun(x):
    """Returns the mode (most common value) of a 1D list input"""
    most_common = None
    highest_count = 0
    vals = set(x)
    # print(vals)
    for i in vals:
        if x.count(i) > highest_count:
            highest_count = x.count(i)
            most_common = i
            # print(f"{i}: {x.count(i)}")
    return most_common

x = random.choices(range(100), k=100)

#** Part a
mean = np.mean(x)
median = np.median(x)
mode = mode_fun(x)

# print(x)
print(f"Mean: {mean:.1f}\nMedian: {median:.1f}\nMode: {mode:.1f}")


#** Part b
vals = set(x)
val_dicts = {}
for i in vals:
    val_dicts[f"{i}"] = x.count(i)

print(f"Dictionary of value: Counts {val_dicts}")


#** Part c
bins = [[]] * 10
counts = [0] * 10

for i in x:
    ind = math.floor(i/10)
    bins[ind] = bins[ind] + [i]
    counts[ind] += 1
    # Check if any 2 bins have the same number of values (greater than 1)
    if counts.count(counts[ind]) >= 2 and counts[ind] > 1:
        break

# print(x)
print(f"Groups: {bins}")
print(f"Counts: {counts}")

