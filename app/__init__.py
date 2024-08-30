from flask import Flask
from config import Config, Development, Production
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Development)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)




from app import routes, models