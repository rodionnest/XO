a = [
    ['1', '2', '3'],
    ['1', '2', '3'],
    ['1', '2', '3'],
]
print(a)

b = a.copy()
print(b)

for i in range(len(b)):
    b[i] = b[i][::-1]

print(a)
print(b)
