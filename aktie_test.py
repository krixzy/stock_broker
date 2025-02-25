import tensorflow as tf
import yfinance as yf
import pandas as pd
from datetime import date, timedelta
from matplotlib import pyplot as plt
import numpy as np



from models.regression_model import RegressionModel

Start = date.today() - timedelta(650)
Start.strftime('%Y-%m-%d')

End = date.today() - timedelta(2)
End.strftime('%Y-%m-%d')

def closing_price(ticker):
    Asset = pd.DataFrame(yf.download(ticker, start=Start,
      end=End))     
    return Asset

def create_dataset(data, window_size=10):
    X, y = [], []
    data = data.values
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size]) 
        y.append(data[i+window_size])  
    return np.array(X).reshape(-1, 10), np.array(y).reshape(-1)



def show_graph(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Stock price')
    plt.title('Stock price')
    plt.xlabel('Days')
    plt.ylabel('Stock price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    spy = closing_price('SPY')
    # show_graph(spy)
    traning_data = spy['Close'][:250]
    test_data = spy['Close'][250:]
    X_train, y_train = create_dataset(traning_data)
    X_test, y_test = create_dataset(test_data)
    model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation="relu", input_shape=(10,)),
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dense(1)
        ])

    model.compile(optimizer="adam", loss="mse")
    history = model.fit(x=X_train, y=y_train, epochs=20, batch_size=2, validation_split=0.2)
    predictions = model.predict(X_test)
    plt.figure(figsize=(10, 5))
    plt.plot(history.history['loss'], label='Træningstab')
    plt.plot(history.history['val_loss'], label='Valideringstab')
    plt.xlabel('Epochs')
    plt.ylabel('Loss (MSE)')
    plt.title('Modelens tab under træning')
    plt.legend()
    plt.show()
    plt.figure(figsize=(10, 6))
    plt.plot(y_test, label='Actual stock', color='blue')
    plt.plot(predictions, label='Expeted stock', color='red')
    plt.title('Actual vs. Expeted stock')
    plt.xlabel('Days')
    plt.ylabel('Stock price')
    plt.legend()
    plt.show()