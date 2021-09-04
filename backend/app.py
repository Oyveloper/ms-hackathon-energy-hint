from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # data = get_consumption_data("707057500100175148", "2019-09-10", "2020-09-10")
    app.run()
