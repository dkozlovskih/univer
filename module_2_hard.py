from random import randint

p1 = randint(3, 20)

p2 = []
for t in range(1, p1):
    for r in range(1, t):

        if p1 % (t+r) == 0:
            p2.append((r, t))

print(p1, '-', p2)

