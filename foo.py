
l = [True,False]
print(any(l))
print(all(l))

def powtwo(x):
    i = 0
    while True:
        yield 2**i
        i += 1

f = powtwo(10)
for i in range(10):
    print(next(f))

try:
    f = open('foofile.txt','rU')
except:
    print('No file found.')

a = [1,2,3]
b = [7,8,9]
print(list(zip(a,b)))
z = zip(a,b)
print(list(zip(*z)))

m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
z = list(zip(m.values(),m.keys()))
m.clear()
for x in z:
    m[x[0]] = x[1]

print(m)

d = {x: 2**x for x in range(5)}
print(d)


