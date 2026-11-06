nlist = [20, 13, 17, 6, 1, 12, 13, 10, 100, 32, 88, 11 , -1, 99, 110, 3, 52]
n = len(nlist)
for i in range(n-1):
    iteration_number = i+1 # because i starts from 0
    # iteration number 1, we need n-1 swaps
    # iteration number 2, we need n-2 swaps
    for j in range(0, n-iteration_number):
        if nlist[j] > nlist[j+1]:
            nlist[j], nlist[j+1] = nlist[j+1], nlist[j]

print(nlist)