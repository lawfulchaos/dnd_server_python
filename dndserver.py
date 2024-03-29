import os

from flask import Flask, json, request, abort
from sqlathanor import initialize_flask_sqlathanor

from database import db

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

from models import Beast, Spell, Item


def search_items(item_list, pattern):
    return item_list.query.filter(
        *[getattr(item_list, col_name).like("%" + pattern[col_name] + "%") for col_name in
          pattern]).all()


def add_to_db(itemlist, itemtype="Spell"):
    translation_table = {"Описание": "description", "Название": "name",
                         "Источник": "source", "Качество": "quality", "Изображения": "images",
                         "Харизма": "charisma", "Чувства": "senses", "Способности": "abilities",
                         "Сопротивление урону": "resistance", "Интеллект": "intelligence",
                         "Сила": "strength", "Легендарные действия": "legendary_acts",
                         "Уязвимость к урону": "vulnerability", "Класс доспеха": "armor_class",
                         "Навыки": "skills", "Мудрость": "wisdom",
                         "Иммунитет к статусу": "status_immunities",
                         "Логово": "lair", "Ловкость": "agility", "Языки": "languages",
                         "Скорость": "speed",
                         "Тип доспеха": "armor_type", "Действия": "actions",
                         "Действия логова": "lair_acts",
                         "Спасброски": "saves", "Эффекты логова": "lair_effects",
                         "Телосложение": "constitution",
                         "Опасность": "danger", "Хиты": "hits", "Кубы хитов": "hit_dice",
                         "Иммунитет к урону": "dmg_immunities", "Реакции": "reactions",
                         'Время накладывания': "cast_time", 'Дистанция': "distance",
                         'Длительность': "time_active", 'Классы': "classes", 'Компоненты':
                             "components", 'Школа': "school", "Уровень": "level"
                         }
    for item in itemlist:
        item["id"] = itemlist.index(item)
        for key in item.copy():
            if key in translation_table:
                if key == "Уровень":
                    item[key] = int(item[key])
                item[translation_table[key]] = item.pop(key)
        if itemtype != "Spell":
            to_add = Beast(**{k: v for k, v in item.items() if
                              k not in {'Магический предмет добавил', "Монстра добавил",
                                        "Заклинание добавил"}})
        else:
            to_add = Spell(**{k: v for k, v in item.items() if
                              k not in {'Магический предмет добавил', "Монстра добавил",
                                        "Заклинание добавил"}})
        db.session.add(to_add)
    db.session.commit()


entry_names = {"spell": Spell, "beast": Beast, "item": Item}


@app.route('/entries/<entries>', methods=['GET'])
def get_entries(entries):
    if entries not in entry_names:
        abort(404)
    pattern = dict(request.args)
    if pattern:
        matching = [item.to_dict(max_nesting=3) for item in search_items(entry_names[entries], pattern)]
        return app.response_class(
            response=json.dumps(matching, ensure_ascii=False),
            mimetype='application/json'
        )

    else:
        items = [item.to_dict(max_nesting=3) for item in entry_names[entries].query.all()]
        return app.response_class(
            response=json.dumps(items, ensure_ascii=False),
            mimetype='application/json'
        )


@app.route('/', methods=['GET'])
def get_welcome():
    return 'Welcome to this unfinished stuff!'
