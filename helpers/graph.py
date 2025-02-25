from matplotlib import pyplot as plt

class Graph:

    @classmethod
    def single_line_graph(cls, data, title = "Graph of data", xlabel = "X-axis", ylabel = "Y-axis", label = "Data"):
        plt.plot(data, label=label)
        cls.set_labels(title, xlabel, ylabel)
        plt.legend()

        plt.show()

    @classmethod
    def multi_line_graph(cls, data, title = "Graph of data", xlabel = "X-axis", ylabel = "Y-axis", labels = ["Data1", "Data2"]):
        for i in range(len(data)):
            plt.plot(data[i], label=labels[i])
        cls.set_labels(title, xlabel, ylabel)
        plt.legend()
        plt.show()

    @classmethod
    def set_labels(cls, title, xlabel, ylabel):
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)