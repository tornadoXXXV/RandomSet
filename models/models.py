from db import db,app

class Menu(db.Model):

    __tablename__ = 'regular_menu'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    cal = db.Column(db.Integer)

@app.before_first_request
def init():
    db.create_all()