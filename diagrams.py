from matplotlib import pyplot as plt


def save_bar(names: list[str], values: list[int], path: str):
    plt.bar(names, values)
    plt.savefig(path)

