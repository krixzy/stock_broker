from models.stock_broker import StockBroker
from models.stock_data import StockData
from models.regression_model import RegressionModel
from helpers.data_converter import DataConverter
from helpers.graph import Graph
class BrokerController:
    def __init__(self, shape = 3):
        self.shape = shape
    
    def run_a_day(self):
        StockBroker("The Broker", self.trained_regression_model())

    def trained_regression_model(self):
        model = RegressionModel.create_model(input_shape=3)
        train_input, train_output = self.data_for_model()
        history = model.train(train_input, train_output, epochs=15, validation_split=0.2)

    def data_for_model(self):
        stock_data = StockData.create_stock_data("SPY", start_day_in_days=200)
        train_input, train_output = DataConverter.convert_data_columns_to_input_and_output_data(stock_data.closing_price(), window_size=self.shape)
        return train_input, train_output