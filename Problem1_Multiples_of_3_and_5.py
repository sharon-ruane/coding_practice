# Problem 1 _ Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def tf_multiple_sum(n):
    multiples = []
    num = n-1
    while num > 0:
        if num %3 == 0 or num %5 == 0:
            multiples.append(num)
        num = num-1
    print(multiples)
    return sum(multiples)

# print(tf_multiple_sum(1000))