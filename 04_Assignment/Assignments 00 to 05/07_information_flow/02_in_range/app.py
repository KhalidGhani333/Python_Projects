

# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def in_range(n, low, high):
    return n >= low and n <= high


print(in_range(21,20,30))
print(in_range(20,20,30))
print(in_range(18,20,30))
print(in_range(31,20,30))