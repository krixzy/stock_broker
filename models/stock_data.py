import pandas as pd
import yfinance as yf
from datetime import date, timedelta


class StockData:
    def __init__(self, data, stock_name, start_date, end_date):
        self.stock_data = pd.DataFrame(data)
        self.stock_name = stock_name
        self.stock_start_date = start_date
        self.stock_end_date = end_date

    def name(self):
        return self.stock_name

    def data(self):
        return self.stock_data

    def start_date(self):
        return self.stock_start_date

    def end_date(self):
        return self.stock_end_date    
    
    def closing_price(self):
        return self.stock_data['Close']
    
    def latest_stock_price(self):
        return self.stock_data['Close'].iloc[-1]
    
    
    @classmethod
    def create_stock_data(cls, stock_name, start_day_in_days=300, end_day_in_days=0):
        start = (date.today() - timedelta(start_day_in_days)).strftime('%Y-%m-%d')
        end = (date.today() - timedelta(end_day_in_days)).strftime('%Y-%m-%d')
        stock_data = yf.download(stock_name, start=start, end=end)
        return cls(stock_data, stock_name, start, end)