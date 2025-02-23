import yfinance as yf


class StockData:
    def __init__(self, data, stock_name):
        self.data =data
        self.stock_name = stock_name

    def name(self):
        return self.stock_name

    def data(self):
        return self.data
    
    @classmethod
    def create_stock_data(cls, stock_name, start_day_in_dayes=0, end_day_in_dayes=300):
        stock_data = yf.download(stock_name, start=start_day_in_dayes, end=end_day_in_dayes)
        return cls(stock_data, stock_name)