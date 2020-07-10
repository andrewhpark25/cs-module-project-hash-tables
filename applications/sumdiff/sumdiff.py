"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

import itertools

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
    


numbers = list(itertools.product(q, q))

for i in numbers:
    for j in numbers:
        if f(i[0]) + f(i[1]) == f(j[0]) - f(j[1]):
            print(f"f({i[0]}) + f({i[1]}) = f({j[0]}) - f({j[1]})" + "    " + str(f(i[0])) + " + " + str(f(i[1])) + " = " + str(f(j[0])) + " - " + str(f(j[1])))