import os

from flask import Flask, json

app = Flask(__name__)


def get_json():
    jsons = {}
    for file in os.listdir("./files"):
        if ".json" in file:
            print(file, "Found")
            jsons[file.split(".")[0]] = json.load(open(file, encoding="utf-8"))
    return jsons


@app.route('/files/<file>', methods=['GET'])
def get_files(file):
    return json.dumps(files[file], ensure_ascii=False)


@app.route('/', methods=['GET'])
def get_welcome():
    return 'Welcome to this unfinished stuff!'


files = get_json()
