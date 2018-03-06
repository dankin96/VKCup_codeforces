'''qty_keepers, qty_defenders, qty_strikers = map(lambda s: int(s), input().split())
array_of_players = list()
for i in range(0, qty_keepers)
    keepers = array_of_playersmap(lambda s: int(s), input().split()), 0
for i in range(0, qty_strikers)
    defenders = map(lambda s: int(s), input().split()), 1
for i in range(0, qty_defenders)
    strikers = map(lambda s: int(s), input().split())
for i in range(1, qty + 1):
    '''
from operator import itemgetter

g, d, f = map(lambda i: int(i), input().split())
players = []
# 0 - вратари
# 1 - защитники
# 2 - нападающие
for p in map(lambda i: int(i), input().split()):
    players.append((p, 0))

for p in map(lambda i: int(i), input().split()):
    players.append((p, 1))

for p in map(lambda i: int(i), input().split()):
    players.append((p, 2))

players.sort(key=itemgetter(0))
i = 0
counter = 0
while i < len(players) - 6:
    j = i + 1
    while players[j][0] < players[i][0] * 2 and j < len(players):
        j = j + 1
    if j - i >= 6:
        keepers = 0
        defenders = 0
        strikers = 0
        for c in range(i, j):
            if players[c][1] == 0:
                keepers = keepers + 1
            elif players[c][1] == 1:
                defenders = defenders + 1
            else:
                strikers = strikers + 1
        if keepers >= 1 and defenders >= 2 and strikers >= 3:
            counter = counter + keepers * (defenders - 1) * (strikers - 2)
    i = i + 1


print(counter)
