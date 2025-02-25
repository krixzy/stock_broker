import tensorflow as tf
import pandas as pd



class RegressionModel:
    def __init__(self, model):
        self.model = model


    def train(self, traning_data, expected_data, epochs=10, batch_size=2, validation_split=0):
        history = self.model.fit(traning_data, expected_data, epochs=epochs, batch_size=batch_size, validation_split=validation_split)
        return history
    
    def predict(self, data):
        return self.model.predict(data)
    

    @classmethod
    def create_model(cls, input_shape=10):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation="relu", input_shape=(input_shape,)),
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dense(1)
        ])

        model.compile(optimizer="adam", loss="mse")
        return cls(model)
    