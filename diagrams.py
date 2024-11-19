from matplotlib import pyplot as plt


def save_bar(names: list[str], values: list[int], path: str):
    plt.bar(names, values)
    plt.savefig(path)


def save_graph(begin: int, end: int, step: int, func: str, path: str):
    x_value = [x for x in range(begin, end, step)]
    y_value = [eval(func) for x in x_value]

    plt.figure(figsize=(8, 6))
    plt.plot(x_value, y_value, label=func)
    plt.title(func)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.legend()
    plt.show()
    print(x_value, y_value)


save_graph(-10, 10, 1, '1', "")
