from collections import deque

sample = [1, 2, 3, 4, 5, 6]
sample.append(7)
lst =[]
# print(sample)
d = deque()
d.append('a')
d.extend(sample)
print(d)
d.rotate(1)
print(d)
d.rotate(-2)
print(d)
print(*d)
d.reverse()
print(d)
d.insert(0,'wow')
print(d)
d.remove('a')
print(d)
d.reverse()
d.extend([1,2,3,4,5,6,7])
print(d)
print(d.index(6,-14,-1))
d.append([1,2])
print(d)