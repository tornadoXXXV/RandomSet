import os
from flask_sqlalchemy import SQLAlchemy
from db import init_db
from menu_controller import menu_blueprint
from db import app

init_db(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{password}@{host}/{name}'.format(**{
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'name': os.getenv('DB_NAME')
})
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
app.config['SQLAlchemy_ECHO'] = False

app.register_blueprint(menu_blueprint)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)