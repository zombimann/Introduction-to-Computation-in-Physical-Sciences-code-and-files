##### CODE BY MUGAMBI NDWIGA, mugambindwiga@gmail.com, +254714103665


"""
===========================================
Problem Statement:

(a) Write a function to determine if n is a prime number. You can assume n is a positive
integer. Is 9,521,928,547 prime?
(b) What is the 104-th prime number?
(c) How many numbers less than 107 are prime?
(d) Plot the ratio nprime/n for 2 < n < 103, where nprime is the number of primes ≤ n.
Describe your results. What would you expect as n continues to increase?

==========================================

I will use the Miller-Rabin algorithm for checking for primality

Reference: Introduction to Algorithms, Third Edition - Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein, pgs 968 - 975

Here's my pseudocode:
function is_prime(n):
    # Handle small cases
    if n < 2: return False
    if n in {2, 3}: return True
    if n % 2 == 0: return False

    # Write n−1 as 2^s * d where d is odd
    d = n - 1
    s = 0
    while d % 2 == 0:
        d = d / 2
        s = s + 1

    # Deterministic bases for 64-bit integers
    bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

    for a in bases:
        if a % n == 0:
            continue   # base n does nothing

        x = pow(a, d) mod n
        if x == 1 or x == n - 1:
            continue

        found_composite = True
        for r in range(1, s):
            x = (x * x) mod n
            if x == n - 1:
                found_composite = False
                break

        if found_composite:
            return False  # definitely composite

    return True  # definitely prime
"""

from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt

#%% Part a

def is_prime(n):
    """
    Check if number is prime
    Return True if prime, else return False
    """
    if n < 2: # 1, 0 and negative are not prime
        return False
    if n in [2, 3]: # 2 and 3 are prime
        return True
    if n % 2 == 0: # Even numbers are not prime (except 2)
        return False

    d = n - 1
    s = 0
    while d % 2 == 0: # Check for evenness
        d = d // 2
        s += 1
    
    # Deterministic bases for 64-bit integers
    bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

    for a in bases:
        if a % n == 0:
            continue # base n does nothing

        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        composites = True
        for _ in range(1, s):
            x = (x * x) % n
            if x == n - 1:
                composites = False
                break

        if composites:
            return False # Definitely composite
        
    return True # Definitely prime


#%% Part b
def number_of_primes():
    num_primes = 0
    i = 0

    while num_primes < 1e4:
        if is_prime(i) == True:
            num_primes += 1
        i += 1
    # print(f"{i-1} : {num_primes}")
    # print(is_prime(i-1))

    print(f"The {num_primes}th prime is {i-1}")


#%% Part c
def count_primes(limit = 1e7):
    start, end = limit
    primes = 0
    for n in range(start, end):
        if is_prime(n) == True:
            primes += 1
    return primes

if __name__ == "__main__": 
    number_of_primes() # 104729
    N = 10_000_000
    workers = cpu_count()  # use all cores
    chunk = N // workers

    ranges = [(i * chunk, (i + 1) * chunk) for i in range(workers)]
    ranges[-1] = (ranges[-1][0], N)  # ensure covering entire range

    with Pool(workers) as p:
        results = p.map(count_primes, ranges)

    # print(results)
    total_primes = sum(results)

    print(f"The number of primes less than {N} is {total_primes}") # 664579

#%% Part d

    N_prime = range(2, 1_000)
    num_primes = []
    for N in N_prime:
        print(N)
        workers = cpu_count()  # use all cores
        chunk = N // workers

        ranges = [(i * chunk, (i + 1) * chunk) for i in range(workers)]
        ranges[-1] = (ranges[-1][0], N)  # ensure covering entire range

        with Pool(workers) as p:
            results = p.map(count_primes, ranges)
        
        num_primes.append(sum(results))

    plt.plot(N_prime, num_primes, 'k-')
    plt.title("Prime Numbers Distribution")
    plt.xlabel("Limit Size (2 to 1000)")
    plt.ylabel("Number of Primes")
    plt.show()
