from flask import Flask
from flask_cors import CORS
from advice.advice_generator import get_all_advice_for_device
from routes.advice import advice

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(advice, url_prefix="/advice")

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
