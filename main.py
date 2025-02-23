import argparse
from stock_data import StockData
from graph import Graph

def command():
    parser = argparse.ArgumentParser(description="This is a simple program that takes a string and returns the string in reverse")
    parser.add_argument("Command", help="Enter what command to run(model_test)")
    args = parser.parse_args()
    return args


def model_test():
    stock_data = StockData.create_stock_data("SPY")
    Graph.single_line_graph(stock_data.closing_price())


if __name__ == "__main__":
    args = command()
    if args.Command == "model_test":
        model_test()
    else:
        print("Invalid command")