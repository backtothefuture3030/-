from functools import reduce
print(reduce(lambda x, y : max(x+y, y+x), sorted(['5', '56', '54', '1200', '12'])))

print(sorted(['5', '56', '54', '1200', '12']))