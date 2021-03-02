import os

from flask import Flask, json


def get_json():
    jsons = {}
    for file in os.listdir("./files"):
        if ".json" in file:
            print(file, "Found")
            jsons[file.split(".")[0]] = json.load(open("./files/" + file, encoding="utf-8"))
    return jsons


app = Flask(__name__)
print("App created")
files = get_json()
print("JSON created")

@app.route('/files/<file>', methods=['GET'])
def get_files(file):
    return json.dumps(files[file], ensure_ascii=False)


@app.route('/', methods=['GET'])
def get_welcome():
    return 'Welcome to this unfinished stuff!'
