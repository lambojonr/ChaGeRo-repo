from flask import Flask

app = Flask(__name__)
app.config.from_object('imagebattle.config')

from flask.ext.sqlalchemy import SQLAlchemy 
db=SQLAlchemy(app)
from . import hooks  # noqa
from . import views  # noqa
from . import model