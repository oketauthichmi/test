import os
d = {'A': {34, 12, 23, 23, 34}, 'B': {37, 42, 33, 29, 64}, 'C': {31, 41, 13, 15, 12}, 'D': {27, 42, 33, 29, 64},
     'E': {11, 51, 63, 25, 27}, 'F': {21, 37, 13, 19, 14}, 'G': {10, 31, 23, 35, 17}}
a = []
b = []
c = []
e = []
for i in d:
    a.append(d.get(i))
for i in a:
    for j in i:
        b.append(j)
# print(a)
for i in a:
    c.append(list(i))
# print(c)
for i in c:
    for j in i:
        print(j, end=" ")
    print()
print("hello word!!!!!!!!11")
hdjghdk