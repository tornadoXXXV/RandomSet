from flask_sqlalchemy import SQLAlchemy
from db import init_db
from menu_controller import menu_blueprint
from db import app

init_db(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:cryout35P@127.0.0.1/postgres'
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
app.config['SQLAlchemy_ECHO'] = False

app.register_blueprint(menu_blueprint)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)