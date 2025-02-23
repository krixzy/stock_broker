import tensorflow as tf
import pandas as pd



class RegressionModel:
    def __init__(self, model):
        self.model = model

    @classmethod
    def create_model(cls):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation="relu", input_shape=(10,)),  # 10 dages input
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dense(1)  # Output: næste dags pris
        ])

        model.compile(optimizer="adam", loss="mse")
        return model
    