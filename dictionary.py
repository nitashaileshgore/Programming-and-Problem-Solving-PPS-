d={1:'a',2:'b'}
print(d)
print(d.keys())
print(d.values())
print(d.items())
for i in d:
    print(i)
for i in d:
    print(d[i])
for i in d.items():
    print(i)
d[1]='c'
print(d)
d[3]='s'
print(d)
d.popitem()
print(d)
