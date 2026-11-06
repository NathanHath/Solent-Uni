nlist = [20, 13, 17, 6, 1, 12, 13, 10, 100, 32, 88, 11 , -1, 99, 110, 3, 52]
for num in nlist:
    for i in range(0, len(nlist)-1):
        if nlist[i] > nlist[i+1]:
            nlist[i], nlist[i+1] = nlist[i+1], nlist[i]

print(nlist)