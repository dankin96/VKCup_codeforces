def ref(i):
    ids.add(i)
    for j in range(1, window + 1):
        if i + j <= qty:
            ids.add(i + j)
        if i - j >= 1:
            ids.add(i - j)
    if references[i - 1] == 0:
        print(len(ids), end=' ')
    else:
        ref(references[i - 1])


qty, window = map(lambda s: int(s), input().split())
references = list()
references = list(map(lambda s: int(s), input().split()))
for i in range(1, qty + 1):
    ids = set()
    ref(i)