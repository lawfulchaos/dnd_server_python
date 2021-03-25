import os
from flask import Flask, json, request, jsonify
from database import db
from sqlathanor import FlaskBaseModel, initialize_flask_sqlathanor

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
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", 'postgres:///app.db')
print("App created")
db.init_app(app)
db = initialize_flask_sqlathanor(db)


def match_values(pattern_key, pattern_value, item_value):
    if pattern_key in INT_VALUES:
        return item_value == int(pattern_value)
    elif pattern_key in STRING_LISTS:
        return any([pattern_value in st for st in STRING_LISTS])
    else:
        return pattern_value in item_value


def search_items(item_list, pattern):
    found = []
    items = item_list.query
    items.filter_by(pattern).all()
    for item in item_list:
        for pattern_key in pattern:
            if pattern_key not in item \
                    or not match_values(pattern_key, pattern[pattern_key], item[pattern_key]):
                break
        else:
            found.append(item)
    return found


#
#
# def add_to_db(itemlist, itemtype="Spell"):
#     translation_table = {"Описание": "description", "Название": "name",
#                          "Источник": "source", "Качество": "quality", "Изображения": "images",
#                          "Харизма": "charisma", "Чувства": "senses", "Способности": "abilities",
#                          "Сопротивление урону": "resistance", "Интеллект": "intelligence",
#                          "Сила": "strength", "Легендарные действия": "legendary_acts",
#                          "Уязвимость к урону": "vulnerability", "Класс доспеха": "armor_class",
#                          "Навыки": "skills", "Мудрость": "wisdom",
#                          "Иммунитет к статусу": "status_immunities",
#                          "Логово": "lair", "Ловкость": "agility", "Языки": "languages",
#                          "Скорость": "speed",
#                          "Тип доспеха": "armor_type", "Действия": "actions",
#                          "Действия логова": "lair_acts",
#                          "Спасброски": "saves", "Эффекты логова": "lair_effects",
#                          "Телосложение": "constitution",
#                          "Опасность": "danger", "Хиты": "hits", "Кубы хитов": "hit_dice",
#                          "Иммунитет к урону": "dmg_immunities", "Реакции": "reactions",
#                          'Время накладывания': "cast_time", 'Дистанция': "distance",
#                          'Длительность': "time_active", 'Классы': "classes", 'Компоненты':
#                              "components", 'Школа': "school"
#                          }
#     for item in itemlist:
#         for key in item.copy():
#             if key in translation_table:
#                 item[translation_table[key]] = item.pop(key)
#         if itemtype != "Spell":
#             to_add = Beast(**{k: v for k, v in item.items() if
#                               k not in {'Магический предмет добавил', "Монстра добавил",
#                                         "Заклинание добавил"}})
#         else:
#             to_add = Spell(**{k: v for k, v in item.items() if
#                               k not in {'Магический предмет добавил', "Монстра добавил",
#                                         "Заклинание добавил"}})
#         db.session.add(to_add)
#     db.session.commit()
from models import Beast, Spell, Item

entry_names = {"spell": Spell, "beast": Beast, "item": Item}


@app.route('/entries/<entries>', methods=['GET'])
def get_entries(entries):
    pattern = dict(request.args)
    if pattern:
        matching = search_items(entry_names[entries], pattern)
        return json.dumps(matching, ensure_ascii=False)
    else:
        items = [item.to_json(ensure_ascii=False) for item in entry_names[entries].query.all()]
        return jsonify(items)


@app.route('/', methods=['GET'])
def get_welcome():
    return 'Welcome to this unfinished stuff!'
