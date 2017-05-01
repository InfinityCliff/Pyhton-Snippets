# Combining tuples
a = (1, 2)
b = (3, 4)
d = (4, 5)

c = (a,) + (b,)
print(c)

e = c + (d,)
print(e)