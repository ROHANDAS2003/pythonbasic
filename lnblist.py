L1 = [11,21,24,12,18]
L2 = [14,44,25,37,13]
L3 = []

for i in L1[0::2]:
    L3.append(i)
for i in L2[1::2]:
    L3.append(i)

print(L3)