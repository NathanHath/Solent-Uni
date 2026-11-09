def likelihood_min_max():
    likelihood = 50, 38, 27, 99, 4
    return min(likelihood), max(likelihood)

def run_task2():
    min, max = likelihood_min_max()
    return (f"Minimum likelihood of falling: {min}%"), (f"maximum likelihood of falling: {max}%")

min, max = run_task2()
print (min,"\n",max)
