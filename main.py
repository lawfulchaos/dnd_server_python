import os

from flask import Flask, json

api = Flask(__name__)


def get_json():
    files = {}
    for file in os.listdir():
        if ".json" in file:
            print(file, "Found")
            files[file.split(".")[0]] = json.load(open(file, encoding="utf-8"))
    return files


@api.route('/files/<file>', methods=['GET'])
def get_files(file):
    return json.dumps(files[file], ensure_ascii=False)


@api.route('/', methods=['GET'])
def get_welcome():
    return 'Welcome to this unfinished stuff!'


if __name__ == '.__main__':
    files = get_json()
    api.run()
