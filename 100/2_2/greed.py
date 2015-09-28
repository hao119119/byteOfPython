v = [1, 5, 10, 50, 100, 500]
c = [0, 0, 2, 4, 3, 1]


def solve(A):
    ans = 0
    for x in range(5, -1, -1):
        t = min(A / v[x], c[x])
        A -= t * v[x]
        ans += t
    print ans


solve(750)

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


def smallest_str():
    S = 'acdbcb'
    T = ''
    head = 0
    end = len(S) - 1
    while head != end:
        for i in range(0, end - head):
            if S[head + i] < S[end - i]:
                left = True
                break
            elif S[head + i] > S[end - i]:
                left = False
                break
        if left:
            T += S[head]
            head += 1
        else:
            T += S[end]
            end -= 1

    T += S[end]
    print T


smallest_str()


def less_mark_point():
    R = 10
    X = [1, 7, 15, 20, 30, 50]
    N = len(X)
    i = 0
    ans = 0
    while i < N:
        s = X[i]
        i += 1
        while i < N and X[i] <= s + R:
            i += 1
        p = X[i-1]
        while i < N and X[i] <= p + R:
            i += 1
        ans += 1

    print ans
less_mark_point()


def cut_less_cost():
    L = [8, 5, 8]
    N = len(L)
    ans = 0
    while N > 1:
        min1 = 0
        min2 = 1
        if L[min1] > L[min2]:
            min1, min2 = min2, min1
        for i in range(2, N):
            if L[i] < L[min1]:
                min1 = i
                min2 = min1
            elif L[i] < L[min2]:
                min2 = i
        t = L[min1] + L[min2]
        ans += t

        if min1 == N-1:
            min1, min2 = min2, min1
        L[min1] = t
        L[min2] = L[N-1]
        N -= 1
    print ans
cut_less_cost()
