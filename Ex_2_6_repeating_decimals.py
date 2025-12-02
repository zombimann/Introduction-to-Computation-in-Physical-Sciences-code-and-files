##### CODE BY MUGAMBI NDWIGA, mugambindwiga@gmail.com, +254714103665

"""
PROBLEM STATEMENT:
Repeating Decimals

Given a rational number n/m, its decimal expansion either repeats or terminates.
Example: 1/11 = 0.(09), 1/2 = 0.5.

Tasks:
1. Implement a function that returns the cycle length L of n/m.
   Terminating decimals have L = 0.

2. Plot L as a function of the denominator d for 1/d, with d = 2...1000.

3. Plot the distribution of L for d = 2...1000.

4. Comment on any patterns observed.

a0 = 3
a = 1 / 3 = 0.33333333333  .....
whole = 1 // 3 = 0
exponent = a - whole = 0.33333333 ....
a = exponent * 10 = 3.3333333  ....
whole = a - exponent = 3
exponent = a - whole = 0.33333333 ....


"""
import math
import matplotlib.pyplot as plt

def repeating_decimals(a0):
    """
    Returns the cycle length of a rational fraction 1/a0 with a0 user-supplied

    For practical purposes, I have included a cut-off of 50 for the cycle length,
    particularly with infintely reapeating decimals in mind.
    """
    if a0 == 1:
        print(1)
        return
    L = -1
    a = 1 / a0 # 0.3333333333

    while True and L <= 50: 
        whole = math.floor(a)  # 0
        exponent = a - whole # 0.3333333333
        # print(f"{whole} : {exponent}")
        if exponent <= 0:
            break
        a = exponent * 10 # 3.333333333
        L += 1
    return L

# #%% Test
# print(repeating_decimals(3))

#%% Simulate
lengths = []
N = 200
for n in range(2,N):
    lengths.append(repeating_decimals(n))

plt.bar(range(2,N), lengths)
plt.xlabel("Numbers")
plt.ylabel("Cycle Length")
plt.title("Numerical Cycle Length Distribution")
plt.show()
