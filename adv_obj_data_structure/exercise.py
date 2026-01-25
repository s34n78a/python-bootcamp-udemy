print(1024, bin(1024), hex(1024))

print()

print(round(5.23222,2))

print()

s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())

print()

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

print()

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))
print(set1.union(set2))

print()

d = {x:x**3 for x in range(5)}
print(d)

print()

list1 = [1,2,3,4]
list1.reverse()
print(list1)

print()

list2 = [3,4,2,5,1]
list2.sort()
print(list2)
