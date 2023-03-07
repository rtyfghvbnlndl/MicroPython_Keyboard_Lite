def index(page, num):
    index = page*15+num
    yield index

a = index(1, 1)
print(a, type(a))
b = next(a)
print(b, type(b))
c = next(a)
print(c, type(c))