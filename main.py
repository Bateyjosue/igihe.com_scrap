# Writen ny Josue Batey

from flask import Flask, request, jsonify #json #jsonify
from flask_cors import CORS
from commons.preprocess import Preprocess
from commons.read import ReadData
from commons.webscrap import WebScrap
from commons.translate import Translate
from commons.regex import Regex

app = Flask(__name__)
CORS(app)

#Init Classes
proprocess = Preprocess()
read = ReadData()
webscrap = WebScrap()
translate = Translate()
regex = Regex()

@app.route('/read')
def read_page():
    """
        Read page
    """
    return f'<h1>{read.info.upper()}<h1>'

@app.route("/initiated_classes_info", methods=["POST"])
def main():
    '''
        Function to load the home pahe
    '''
    data = request.get_json()
    print("data:", data)
    class_info = {
        "preprocess": proprocess.info,
        "read": read.info,
        "webscrap": webscrap.info,
        "translate": translate.info,
        "regex": regex.info
    }
    return {"data": data, "class_info" : class_info}

if __name__ == '__main__':
    app.run()