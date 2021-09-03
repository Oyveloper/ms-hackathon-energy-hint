import json

import matplotlib.pyplot as plt
from flask import Flask

from predictor.train_network import fit_model_to_data, get_prediction

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.get("/prediction")
def prediction():
    model = fit_model_to_data()
    pred = get_prediction(model)

    model.plot(pred)

    return json.dumps(pred.tail(12).loc[:, "yhat"].values.tolist())


if __name__ == '__main__':
    model = fit_model_to_data()
    pred = get_prediction(model)

    model.plot(pred)
    plt.show()
    # app.run()
