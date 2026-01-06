s={1,2,3,4,45,34,55,2,3}
print(s)
# this function is used in empty set().
g=set()
print(type(g))
# union
a={1,2,3,4,5,6,7,7}
b={23,34,54,23,45,67}
a.union(b)
print(a.union(b))
#intersection
a.intersection(b)
print(a.intersection(b))
a.difference(b)
print(a.difference(b))
a.update(b)
print(a.update(b))
b.remove(23)
print(b.remove())