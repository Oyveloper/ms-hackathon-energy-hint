from flask import Flask

from advice.advice_generator import get_all_advice_for_device

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    print(f"Advice: {get_all_advice_for_device('707057500100175148')}")

    app.run()
