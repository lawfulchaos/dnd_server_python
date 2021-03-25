from flask_sqlalchemy import SQLAlchemy
from sqlathanor import FlaskBaseModel

db = SQLAlchemy(model_class=FlaskBaseModel)
