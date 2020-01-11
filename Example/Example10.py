vec1 = [2, 4, -6]
vec2 = [1, -3, -7]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print(x**2 for x in vec1)
print(x*2 for x in vec2)
print([vec1[i]*vec2[i] for i in range(len(vec1))])
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(str(dict))
