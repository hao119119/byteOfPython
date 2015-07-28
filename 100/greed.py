task1 = [1, 2]
task2 = [2, 4]
task3 = [2, 3]
task4 = [4, 6]
task_list = [task1, task2, task3, task4]


def compare(task_a, task_b):
    return task_a[1] - task_b[1]

task_list.sort(cmp=compare)
print task_list

t = 0
ans = 0

for task in task_list:
    if t <= task[0]:
        ans += 1
        t = task[1]

print ans