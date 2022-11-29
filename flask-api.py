from flask import Flask, jsonify, make_response
import os

app = Flask(__name__)
servertype = os.environ['AWS_REGION']


@app.route("/")
def hello_from_root():
    return 'Hello world'

@app.route("/type")
def server_type():
    return f'Hello -{servertype}'


if __name__=="__main__":
    app.run()