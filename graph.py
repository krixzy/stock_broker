from matplotlib import pyplot as plt

class Graph:

    @classmethod
    def single_line_graph(cls, data, title = "Graph of data", xlabel = "X-axis", ylabel = "Y-axis", label = "Data"):
        plt.plot(data, label=label)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()