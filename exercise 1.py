import random
s = 0
for j in range(1000):
    p = [[random.randint(1,80) for i in range(5)] for i in range(100)]
    win = False
    r = []
    while win == False:
        R = random.randint(1,80)
        if R not in r:
            r.append(R)
            for player in p:
                if R in player:
                    player.remove(R)
                    if player == []:
                        win = True
                        break
    s = s + len(r)
print(int(s/1000))