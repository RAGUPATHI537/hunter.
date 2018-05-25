from itertools import permutations
d=input()
l = list(permutations(d))
for x in l:
    print(''.join(x))
