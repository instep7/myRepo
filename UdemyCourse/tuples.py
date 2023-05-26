# Tuples are immutable

tup = ("oranges", "apples", "bananas")
print(tup)

tup2 = (12, 14)
print(tup2)

tup3 = tup + tup2
print(tup3)

print(tup[0], tup2[1], tup3[2])