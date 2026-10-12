num_bars = int(input("enter the number of charging bars\n"))
bars_charged = 0
while bars_charged < num_bars:
    bars_charged += 1
    print ("charging:","█" * bars_charged)
