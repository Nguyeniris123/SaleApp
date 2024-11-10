from sqlalchemy import Column, Integer, String, Float
from app import db, app

class Category(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable =False, unique=True)

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        c1 = Category(name='Mobile')
        c2 = Category(name='Tablet')
        c3 = Category(name='Laptop')
        db.session.add_all([c1, c2, c3])
        db.session.commit()