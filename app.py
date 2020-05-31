from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://35.220.187.253:27017/lda_model"

mongo = MongoClient(host='35.220.187.253', port=27017)
db  = mongo['lda_model']

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
