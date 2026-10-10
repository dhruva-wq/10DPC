#Day 5 pratice

task = ["eat", "code", "sleep"]
print(task)



#Assignment


task.append("repeat")
print(task)

for i in task:
    print(i)
    if i == "code":
        print("Code is there")
    else:
        print("Ok")
else:
    print("Done")

task.copy()
print(task)

task.reverse()
print(task)

task.clear()
print(task)

task.count("code")
print(task.count("code"))

task.extend
print(task.extend(["code", "sleep", "eat"]))

task.index("code")
print(task.index("code"))

task.insert(1, "code")
print(task)

task.pop()
print(task)

task.remove("code")
print(task)

task.sort()
print(task)

task.remove
print(task.remove("code"))

task.sort(reverse=True)
print(task)

task.insert(0, "eat")
task.insert(1, "sleep")
task.insert(2, "code")
print(task)