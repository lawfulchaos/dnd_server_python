from manage import db

INT_VALUES = {"Интеллект", "Опасность", "Класс доспеха", "Сила", "Телосложение", "Харизма",
              "Мудрость",
              "Ловкость", "Хиты"}
# id = db.Column("id", db.Integer, primary_key=True)
# name = db.Column("name", db.String, unique=True)
# cast_time = db.Column("cast_time", db.String)
# distance = db.Column("distance", db.String)
# time_active = db.Column("time_active", db.String)
# source = db.Column("source", db.String)
# classes = db.Column("classes", db.String)
# components = db.Column("components", db.String)
# school = db.Column("school", db.String)
# danger = db.Column("danger", db.Float)


class Spell(db.Model):
    __tablename__ = 'spells'

    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String, unique=True)
    cast_time = db.Column("cast_time", db.String)
    distance = db.Column("distance", db.String)
    time_active = db.Column("time_active", db.String)
    source = db.Column("source", db.String)
    classes = db.Column("classes", db.String)
    components = db.Column("components", db.String)
    school = db.Column("school", db.String)
    description = db.Column("description", db.Text)

    def __repr__(self):
        return '<Spell %r>' % self.name
