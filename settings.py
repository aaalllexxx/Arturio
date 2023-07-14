from flask_sqlalchemy import SQLAlchemy
from app import MyApp

import os

app = MyApp()
base_dir = os.path.dirname(os.path.realpath(__file__))

app.set_root_folder(base_dir)
app.app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(base_dir, 'data.db')
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app.app)
with app.app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run()
