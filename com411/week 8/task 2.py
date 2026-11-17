import matplotlib.pyplot as plt

def small():
    x = [10, 20, 20, 10, 10]
    y = [10, 10, 20, 20, 10]
    plt.plot(x, y, 'ro--')

def medium():
    x = [15, 25, 25, 15, 15]
    y = [15, 15, 25, 25, 15]
    plt.plot(x, y, 'gs--')
def large():
    x = [20, 30, 30, 20, 20]
    y = [20, 20, 30, 30, 20]
    plt.plot(x, y, 'b-p')

def run_task2():
    small()
    medium()
    large()
    plt.show()

run_task2()


