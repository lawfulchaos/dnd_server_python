import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, json, request

INT_VALUES = {"Интеллект", "Опасность", "Класс доспеха", "Сила", "Телосложение", "Харизма",
              "Мудрость",
              "Ловкость", "Хиты"}
STRING_LISTS = {"Действия", "Описание", "Действия логова", "Логово", "Способности", "Изображения"}


def get_json():
    jsons = {}
    for file in os.listdir("./files"):
        if ".json" in file:
            print(file, "Found")
            jsons[file.split(".")[0]] = json.load(open("./files/" + file, encoding="utf-8"))
    return jsons


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", 'sqlite:///app.db')
print("App created")
FILES = get_json()
db = SQLAlchemy(app)
print("JSON created")


def match_values(pattern_key, pattern_value, item_value):
    if pattern_key in INT_VALUES:
        return item_value == int(pattern_value)
    elif pattern_key in STRING_LISTS:
        return any([pattern_value in st for st in STRING_LISTS])
    else:
        return pattern_value in item_value


def search_items(item_list, pattern):
    found = []
    for item in item_list:
        for pattern_key in pattern:
            if pattern_key not in item \
                    or not match_values(pattern_key, pattern[pattern_key], item[pattern_key]):
                break
        else:
            found.append(item)
    return found


@app.route('/files/<file>', methods=['GET'])
def get_files(file):
    pattern = dict(request.args)
    if pattern:
        matching = search_items(FILES[file], pattern)
        return json.dumps(matching, ensure_ascii=False)
    else:
        db.query_expression()
        return json.dumps(FILES[file], ensure_ascii=False)


@app.route('/', methods=['GET'])
def get_welcome():
    return 'Welcome to this unfinished stuff!'
