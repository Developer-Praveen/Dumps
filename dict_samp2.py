# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

#sorted(xs.items(), key=lambda x: x[1])

xss = sorted(xs.items(), key=lambda x: x[1])

#[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

print('XS   : ', xs)

print('XSS  : ', xss)

# Or:

import operator

#sorted(xs.items(), key=operator.itemgetter(1))

xsss = sorted(xs.items(), key=operator.itemgetter(1))

#[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

print('XSSS : ', xsss)