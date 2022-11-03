# Writen ny Josue Batey

from flask import Flask, request, json, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/webscrap", methods=["POST"])
def main():
    '''
        Function to load the home pahe
    '''
    data = request.get_json()
    print("data:", data)
    return {"data": data}, 200

if __name__ == '__main__':
    app.run()