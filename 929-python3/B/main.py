n, k = map(lambda i: int(i), input().split())
rows = []
seats = [0 for _ in range(3)]
required_seats = []
neighbors = 0
for _ in range(n):
    row = []
    prev = None
    for seat in list(input()):
        if seat == 'S' and (prev == 0 or prev == 1):
            row[-1] += 1
            seats[prev] -= 1
            seats[prev + 1] += 1
        elif seat == 'S' and (prev == 'S' or prev == 'P'):
            neighbors += 1
        if (seat == 'S' or seat == 'P') and prev == 'S':
            neighbors += 1
        if seat == '.' and prev == 'S':
            seat = 1
            seats[1] += 1
        elif seat == '.' and prev != 'S':
            seat = 0
            seats[0] += 1
        row.append(seat)
        prev = seat
    rows.append(row)

for s in seats:
    if k < 0:
        k = 0
    required_seats.append(min(k, s))
    k = k - s

print(neighbors + required_seats[1] + required_seats[2] * 2)
for row in rows:
    for c in row:
        if type(c) == int and required_seats[c] > 0:
            required_seats[c] -= 1
            c = 'x'
        elif type(c) == int:
            c = '.'
        print(c, end='')
    print()
