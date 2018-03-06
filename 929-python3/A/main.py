qty, window = map(lambda s: int(s), input().split())
x = list(map(lambda s: int(s), input().split()))
counter = 0
first_x = x[0]
flag = False
i = 1
while i < qty:
    if (first_x + window) >= x[i] and not flag:
        counter = counter + 1
        flag = True
    elif (first_x + window) < x[i] and flag:
        first_x = x[i - 1]
        i = i - 1
        flag = False
    i = i + 1

if not flag:
    print('-1')
else:
    print(counter)