#FORLOOP
'''
for i in range(0, 10):
    print(i)

list = ['a', 'b', 5, 6]
for i in list:
    print(i)
'''

#Assignment


keys = ["name", "role", "exp"]
values = ["Dhruv", "Data Engineer", 4.5]

result = {}   # empty dict create pannunga

for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)