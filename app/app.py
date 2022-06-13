from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

import app.views


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning


db = SQLAlchemy(app)
db.create_all()