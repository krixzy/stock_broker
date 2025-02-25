import argparse
from models.stock_data import StockData
from helpers.graph import Graph
from models.regression_model import RegressionModel
from helpers.data_converter import DataConverter
from controller.broker_controller import BrokerController
import numpy as np

def command():
    parser = argparse.ArgumentParser(description="This is a simple program that takes a string and returns the string in reverse")
    parser.add_argument("Command", help="Enter what command to run(model_test, run_a_day)")
    args = parser.parse_args()
    return args


def model_test():
    stock_data = StockData.create_stock_data("SPY", start_day_in_days=350)
    regresion_model = RegressionModel.create_model(input_shape=3)
    train, test = DataConverter.convert_a_data_columns_to_training_and_test_data(stock_data.closing_price(), split_value=0.8)
    train_input, train_output = DataConverter.convert_data_columns_to_input_and_output_data(train, window_size=3)
    test_input, test_output = DataConverter.convert_data_columns_to_input_and_output_data(test, window_size=3)
    history = regresion_model.train(train_input, train_output, epochs=15, validation_split=0.2)
    Graph.multi_line_graph( [history.history['loss'], history.history['val_loss']], labels=['Training loss', 'Validation loss'], title='Model loss during training', xlabel='Epochs', ylabel='Loss (MSE)')
    resault = regresion_model.predict(test_input)
    Graph.multi_line_graph([test_output, resault], labels=['Actual stock', 'Predicted stock'], title='Actual stock vs Predicted stock', xlabel='Days', ylabel='Stock price')


def run_a_day():
    BrokerController.run_a_day()
    print("Done")


if __name__ == "__main__":
    args = command()
    if args.Command == "model_test":
        model_test()
    elif args.Command == "run_a_day":
        run_a_day()
    else:
        print("Invalid command")