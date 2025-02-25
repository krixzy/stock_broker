import pandas as pd
import numpy as np


class DataConverter:

    @staticmethod
    def convert_a_data_columns_to_training_and_test_data(data_to_split, split_value=0.8):
        split = int(len(data_to_split) * split_value)
        return data_to_split[:split], data_to_split[split:]
    
    @staticmethod
    def convert_data_columns_to_input_and_output_data(data, window_size=10):
        input_data = []
        output_data = []
        data = data.values
        for i in range(len(data) - window_size):
            input_data.append(data[i:i+window_size])
            output_data.append(data[i+window_size])
        return np.array(input_data), np.array(output_data)