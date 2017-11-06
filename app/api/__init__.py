import os
from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)
ma = Marshmallow(db)
api = Api(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

import api.views