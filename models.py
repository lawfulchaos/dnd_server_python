from database import db

INT_VALUES = {"Интеллект", "Опасность", "Класс доспеха", "Сила", "Телосложение", "Харизма",
              "Мудрость",
              "Ловкость", "Хиты"}


class Beast(db.Model):
    __tablename__ = 'beasts'

    id = db.Column("id", db.Integer, primary_key=True,
                   supports_json=True,
                   supports_yaml=True,
                   supports_dict=True,
                   on_serialize=None,
                   on_deserialize=None)
    name = db.Column("name", db.String, unique=True, supports_json=True,
                     supports_yaml=True,
                     supports_dict=True,
                     on_serialize=None,
                     on_deserialize=None)
    hit_dice = db.Column("hit_dice", db.String, nullable=False, supports_json=True,
                         supports_yaml=True,
                         supports_dict=True,
                         on_serialize=None,
                         on_deserialize=None)
    dmg_immunities = db.Column("dmg_immunities", db.String, nullable=True, supports_json=True,
                               supports_yaml=True,
                               supports_dict=True,
                               on_serialize=None,
                               on_deserialize=None)
    abilities = db.Column("abilities", db.ARRAY(db.String), nullable=True, supports_json=True,
                          supports_yaml=True,
                          supports_dict=True,
                          on_serialize=None,
                          on_deserialize=None)
    source = db.Column("source", db.String, nullable=False, supports_json=True,
                       supports_yaml=True,
                       supports_dict=True,
                       on_serialize=None,
                       on_deserialize=None)
    armor_type = db.Column("armor_type", db.String, nullable=False, supports_json=True,
                           supports_yaml=True,
                           supports_dict=True,
                           on_serialize=None,
                           on_deserialize=None)
    status_immunities = db.Column("status_immunities", db.String, nullable=True,
                                  supports_json=True,
                                  supports_yaml=True,
                                  supports_dict=True,
                                  on_serialize=None,
                                  on_deserialize=None)
    skills = db.Column("skills", db.String, nullable=True, supports_json=True,
                       supports_yaml=True,
                       supports_dict=True,
                       on_serialize=None,
                       on_deserialize=None)
    intelligence = db.Column("intelligence", db.Float, nullable=False, supports_json=True,
                             supports_yaml=True,
                             supports_dict=True,
                             on_serialize=None,
                             on_deserialize=None)
    legendary_acts = db.Column("legendary_acts", db.ARRAY(db.String), nullable=True,
                               supports_json=True,
                               supports_yaml=True,
                               supports_dict=True,
                               on_serialize=None,
                               on_deserialize=None)
    lair_acts = db.Column("lair_acts", db.ARRAY(db.String), nullable=True, supports_json=True,
                          supports_yaml=True,
                          supports_dict=True,
                          on_serialize=None,
                          on_deserialize=None)
    danger = db.Column("danger", db.Float, nullable=False, supports_json=True,
                       supports_yaml=True,
                       supports_dict=True,
                       on_serialize=None,
                       on_deserialize=None)
    armor_class = db.Column("armor_class", db.Integer, nullable=False, supports_json=True,
                            supports_yaml=True,
                            supports_dict=True,
                            on_serialize=None,
                            on_deserialize=None)
    lair_effects = db.Column("lair_effects", db.ARRAY(db.String), nullable=True,
                             supports_json=True,
                             supports_yaml=True,
                             supports_dict=True,
                             on_serialize=None,
                             on_deserialize=None)
    vulnerability = db.Column("vulnerability", db.String, nullable=True, supports_json=True,
                              supports_yaml=True,
                              supports_dict=True,
                              on_serialize=None,
                              on_deserialize=None)
    languages = db.Column("languages", db.String, nullable=True, supports_json=True,
                          supports_yaml=True,
                          supports_dict=True,
                          on_serialize=None,
                          on_deserialize=None)
    speed = db.Column("speed", db.String, nullable=False, supports_json=True,
                      supports_yaml=True,
                      supports_dict=True,
                      on_serialize=None,
                      on_deserialize=None)
    resistance = db.Column("resistance", db.String, nullable=True, supports_json=True,
                           supports_yaml=True,
                           supports_dict=True,
                           on_serialize=None,
                           on_deserialize=None)
    strength = db.Column("strength", db.Float, nullable=False, supports_json=True,
                         supports_yaml=True,
                         supports_dict=True,
                         on_serialize=None,
                         on_deserialize=None)
    saves = db.Column("saves", db.String, nullable=True, supports_json=True,
                      supports_yaml=True,
                      supports_dict=True,
                      on_serialize=None,
                      on_deserialize=None)
    description = db.Column("description", db.String, nullable=True, supports_json=True,
                            supports_yaml=True,
                            supports_dict=True,
                            on_serialize=None,
                            on_deserialize=None)
    lair = db.Column("lair", db.String, nullable=True, supports_json=True,
                     supports_yaml=True,
                     supports_dict=True,
                     on_serialize=None,
                     on_deserialize=None)
    constitution = db.Column("constitution", db.Float, nullable=False, supports_json=True,
                             supports_yaml=True,
                             supports_dict=True,
                             on_serialize=None,
                             on_deserialize=None)
    charisma = db.Column("Charisma", db.Float, nullable=False, supports_json=True,
                         supports_yaml=True,
                         supports_dict=True,
                         on_serialize=None,
                         on_deserialize=None)
    agility = db.Column("Agility", db.Float, nullable=False, supports_json=True,
                        supports_yaml=True,
                        supports_dict=True,
                        on_serialize=None,
                        on_deserialize=None)
    wisdom = db.Column("wisdom", db.Float, nullable=False, supports_json=True,
                       supports_yaml=True,
                       supports_dict=True,
                       on_serialize=None,
                       on_deserialize=None)
    hits = db.Column("hits", db.Integer, nullable=False, supports_json=True,
                     supports_yaml=True,
                     supports_dict=True,
                     on_serialize=None,
                     on_deserialize=None)
    reactions = db.Column("reactions", db.ARRAY(db.String), nullable=True, supports_json=True,
                          supports_yaml=True,
                          supports_dict=True,
                          on_serialize=None,
                          on_deserialize=None)
    actions = db.Column("actions", db.ARRAY(db.String), nullable=True, supports_json=True,
                        supports_yaml=True,
                        supports_dict=True,
                        on_serialize=None,
                        on_deserialize=None)
    senses = db.Column("senses", db.String, nullable=True, supports_json=True,
                       supports_yaml=True,
                       supports_dict=True,
                       on_serialize=None,
                       on_deserialize=None)

    def __repr__(self):
        return '<Beast %r>' % self.name


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column("id", db.Integer, primary_key=True, supports_json=True,
                   supports_yaml=True,
                   supports_dict=True,
                   on_serialize=None,
                   on_deserialize=None)
    name = db.Column("name", db.String, unique=True, supports_json=True,
                     supports_yaml=True,
                     supports_dict=True,
                     on_serialize=None,
                     on_deserialize=None)
    source = db.Column("source", db.String, nullable=False, supports_json=True,
                       supports_yaml=True,
                       supports_dict=True,
                       on_serialize=None,
                       on_deserialize=None)
    quality = db.Column("quality", db.String, nullable=False, supports_json=True,
                        supports_yaml=True,
                        supports_dict=True,
                        on_serialize=None,
                        on_deserialize=None)
    images = db.Column("images", db.ARRAY(item_type=db.String), nullable=True, supports_json=True,
                       supports_yaml=True,
                       supports_dict=True,
                       on_serialize=None,
                       on_deserialize=None)
    description = db.Column("description", db.String, nullable=False, supports_json=True,
                            supports_yaml=True,
                            supports_dict=True,
                            on_serialize=None,
                            on_deserialize=None)

    def __repr__(self):
        return '<Item %r>' % self.name


class Spell(db.Model):
    __tablename__ = 'spells'

    id = db.Column("id", db.Integer, primary_key=True, supports_json=True,
                   supports_yaml=True,
                   supports_dict=True,
                   on_serialize=None,
                   on_deserialize=None)
    name = db.Column("name", db.String, unique=True, supports_json=True,
                     supports_yaml=True,
                     supports_dict=True,
                     on_serialize=None,
                     on_deserialize=None)
    cast_time = db.Column("cast_time", db.String, supports_json=True,
                          supports_yaml=True,
                          supports_dict=True,
                          on_serialize=None,
                          on_deserialize=None)
    distance = db.Column("distance", db.String, supports_json=True,
                         supports_yaml=True,
                         supports_dict=True,
                         on_serialize=None,
                         on_deserialize=None)
    time_active = db.Column("time_active", db.String, supports_json=True,
                            supports_yaml=True,
                            supports_dict=True,
                            on_serialize=None,
                            on_deserialize=None)
    source = db.Column("source", db.String, supports_json=True,
                       supports_yaml=True,
                       supports_dict=True,
                       on_serialize=None,
                       on_deserialize=None)
    classes = db.Column("classes", db.String, supports_json=True,
                        supports_yaml=True,
                        supports_dict=True,
                        on_serialize=None,
                        on_deserialize=None)
    components = db.Column("components", db.String, supports_json=True,
                           supports_yaml=True,
                           supports_dict=True,
                           on_serialize=None,
                           on_deserialize=None)
    school = db.Column("school", db.String, supports_json=True,
                       supports_yaml=True,
                       supports_dict=True,
                       on_serialize=None,
                       on_deserialize=None)
    description = db.Column("description", db.Text, supports_json=True,
                            supports_yaml=True,
                            supports_dict=True,
                            on_serialize=None,
                            on_deserialize=None)

    def __repr__(self):
        return '<Spell %r>' % self.name
