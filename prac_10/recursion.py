"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,    3
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n <= 0:
        return 0
    else:
        print(n**2)
    return do_something(n - 1)

# TODO: 3. write down what you think the output of do_something(4) will be,
# will continue to reduce n by 1 until it hits a program limit which will crash the running
# TODO: 4. use the debugger to step through and see what's actually happening
do_something(4)

# TODO: 5. fix do_something() so that it works according to the docstring
blocks = 0
for n in range(0, 7, 1):
    blocks += n
print(blocks)


def do_block_count(n):
    """Prints blocks based on rows"""
    if n <= 0:
        return 0
    return n + do_block_count(n-1)

print(do_block_count(6))