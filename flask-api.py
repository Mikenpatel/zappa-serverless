from flask import Flask, jsonify, make_response
import os
import pymongo



connection="mongodb+srv://Miken:Miken001@multi-region.ilmvkvm.mongodb.net/?retryWrites=true&w=majority"

# set a 5-second connection timeout
client = pymongo.MongoClient(connection, serverSelectionTimeoutMS=5000)

mydb =client["sample_airbnb"]
mycol = mydb["listingsAndReviews"]




try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")

app = Flask(__name__)
servertype = os.environ['AWS_REGION']


@app.route("/")
def hello_from_root():
    return 'Hello world'

@app.route("/type")
def server_type():
    return f'Hello -{servertype}'

@app.route("/data")
def mongo():
    x = mycol.find_one()
    k=x['name']
    return jsonify({"name":k})

if __name__=="__main__":
    app.run()