a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(1))
a.append(433)
a.insert(0, 333)
for i in a:
    print(i, end=" ")

a.sort()  # 从小到大排序
print(a)
a.reverse()  # 翻转
print(a)
print(a.pop())
print(a.pop())
print(a)
