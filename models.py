from manage import db

INT_VALUES = {"Интеллект", "Опасность", "Класс доспеха", "Сила", "Телосложение", "Харизма",
              "Мудрость",
              "Ловкость", "Хиты"}


class Beast(db.Model):
    __tablename__ = 'beasts'

    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String, unique=True)
    hit_dice = db.Column("hit_dice", db.String, nullable=False)
    dmg_immunities = db.Column("dmg_immunities", db.String, nullable=True)
    abilities = db.Column("abilities", db.ARRAY(db.String), nullable=True)
    source = db.Column("source", db.String, nullable=False)
    armor_type = db.Column("armor_type", db.String, nullable=False)
    status_immunities = db.Column("status_immunities", db.String, nullable=True)
    skills = db.Column("skills", db.String, nullable=True)
    intelligence = db.Column("intelligence", db.Float, nullable=False)
    legendary_acts = db.Column("legendary_acts", db.ARRAY(db.String), nullable=True)
    lair_acts = db.Column("lair_acts", db.ARRAY(db.String), nullable=True)
    danger = db.Column("danger", db.Float, nullable=False)
    armor_class = db.Column("armor_class", db.Integer, nullable=False)
    lair_effects = db.Column("lair_effects", db.ARRAY(db.String), nullable=True)
    vulnerability = db.Column("vulnerability", db.String, nullable=True)
    languages = db.Column("languages", db.String, nullable=True)
    speed = db.Column("speed", db.String, nullable=False)
    resistance = db.Column("resistance", db.String, nullable=True)
    strength = db.Column("strength", db.Float, nullable=False)
    saves = db.Column("saves", db.String, nullable=True)
    description = db.Column("description", db.String, nullable=True)
    lair = db.Column("lair", db.String, nullable=True)
    constitution = db.Column("constitution", db.Float, nullable=False)
    charisma = db.Column("Charisma", db.Float, nullable=False)
    agility = db.Column("Agility", db.Float, nullable=False)
    wisdom = db.Column("wisdom", db.Float, nullable=False)
    hits = db.Column("hits", db.Integer, nullable=False)
    reactions = db.Column("reactions", db.ARRAY(db.String), nullable=True)
    actions = db.Column("actions", db.ARRAY(db.String), nullable=True)
    senses = db.Column("senses", db.String, nullable=True)

    def __repr__(self):
        return '<Beast %r>' % self.name


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String, unique=True)
    source = db.Column("source", db.String, nullable=False)
    quality = db.Column("quality", db.String, nullable=False)
    images = db.Column("images", db.ARRAY(item_type=db.String), nullable=True)
    description = db.Column("description", db.String, nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.name


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
