##### CODE BY MUGAMBI NDWIGA, mugambindwiga@gmail.com, +254714103665




import math
import matplotlib.pyplot as plt


def collatz(a):
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

