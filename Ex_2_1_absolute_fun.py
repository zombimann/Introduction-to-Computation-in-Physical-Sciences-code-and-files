##### CODE BY MUGAMBI NDWIGA, mugambindwiga@gmail.com, +254714103665



"""2.1. A generalized absolute value function. We implemented a basic version of f (x) = |x|
in Sect.2.6 that acts on a scalar number x. Extend the function so that it can also operate
on a list of numbers as input and return a list of absolute values as output. Print the
elements and their index where an absolute value cannot be calculated, and remove
them from the final output. The following are expected behavior:
In [117]: abs_val(-2)
Out[117]: 2
In [118]: abs_val([-1, 'not_a_number', -3])
Out[118]: Warning: Dropping input index 1, cannot calculate abs of
'not_a_number' [1, 3]"""

#%% Define function

def abs_val(x):
    y = []
    try:
        for i in range(len(x)):
            try:
                y.append(abs(x[i]))
            except: # In case element is not numeric
                print(f"Warning: Dropping input index {i}, cannot calculate abs of {x[i]}")
                # del(x[i])
    except TypeError: # In case input is not list
            y = abs(x)
    print(y)

#%% Testing
abs_val(-2)

abs_val([-1, 'not_a_number', -3])





