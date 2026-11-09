def likelihood():
    likelihood = 50, 38, 27, 99, 4
    return min(likelihood)

def run_task1():
    return (f"Minimum likelihood of falling: {likelihood()}%")

print(run_task1())