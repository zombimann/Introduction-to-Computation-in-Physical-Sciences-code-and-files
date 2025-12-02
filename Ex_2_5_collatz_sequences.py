##### CODE BY MUGAMBI NDWIGA, mugambindwiga@gmail.com, +254714103665

"""
PROBLEM STATEMENT:

Collatz Sequences

Define the sequence from a positive integer a0 by:
a_{i+1} = a_i/2      if a_i is even
a_{i+1} = 3*a_i + 1  if a_i is odd

All sequences are conjectured to reach 1.
Sequence length L = number of terms until 1 appears.
Example: a0 = 10 → [10, 5, 16, 8, 4, 2, 1], L = 7.

Consider a0 = 2, 3, ..., 10^6.

(a) Identify the a0 producing the longest sequence and its length L.

(b) Plot L vs a0 for a0 < 10^4.
    Plot the distribution of L for 2 ≤ a0 ≤ 10^6.

(c) Let n_odd = count of odd terms (excluding 1).
    Let n_even = count of even terms.
    Compute r = n_odd / n_even.
    Plot r vs a0 for 2 < a0 < 10^4.
    Plot the distribution of r for 2 < a0 ≤ 10^6.
    Show that r is bounded above by log(2) / log(3) for a0 > 2.

"""


import math
import matplotlib.pyplot as plt


def collatz(a):
    """
    This finds the collatz length of a value
    """
    length = 1
    nodd = 0
    neven = 0
    while a > 1:
        length += 1
        # print(a)
        if a % 2 == 0:
            a //= 2
            neven += 1
        else:
            a = 3*a + 1
            nodd += 1
    return a, length, nodd, neven

#%% Test

# a0 = 10
# a1, L = collatz(a0)
# print(f"Initial Value: {a0} | Final Value: {a1} | Length: {L}")

# #%% Part a
# L = 0
# longest_sequence = None
# longest_length = -math.inf
# for n in range(2, 1_000_000):
#     _, L = collatz(n)
#     if L > longest_length:
#         longest_length = L
#         longest_sequence = n


# print(f"Longest Sequence Value: {longest_sequence}   Longest Sequence Length: {longest_length}") # Value: 837799   Length: 525

#%% Part B
L = 0
values = range(2, 200)
lengths, even_odd_ratio = [], []
for n in values:
    _, L, nodd, neven  = collatz(n)
    lengths.append(L)
    even_odd_ratio.append(nodd / neven)
# print(lengths)

plt.plot(values, lengths, 'k-')
# plt.stem(values, lengths)
plt.title("Collatzs Sequence Length Distribution")
plt.ylabel("Sequence Length")
plt.xlabel("Values")
# plt.show()

#%% Part c
plt.figure()
plt.plot(values, even_odd_ratio)
plt.xlabel("Values")
plt.ylabel("Odd / Even Ratio")
plt.title("Distribution of Collatz Ratios")
plt.show()

