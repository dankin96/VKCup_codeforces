def ref(i):
    ids = set()
    ids.add(i)
    for j in range(1, window + 1):
        if i + j <= qty:
            ids.add(i + j)
        else:
            break
    for j in range(1, window + 1):
        if i - j >= 1:
            ids.add(i - j)
        else:
            break
    idsets[i - 1] = ids | idsets[references[i - 1] - 1]
    print(len(idsets[i - 1]), end=' ')


qty, window = map(lambda s: int(s), input().split())
idsets = [set() for index in range(qty)]
references = list(map(lambda s: int(s), input().split()))
for i in range(1, qty + 1):
    ref(i)