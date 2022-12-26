import sqlite3
from db import db


class storeModel(db.Model):

    __tablename__='stores'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))

    items=db.relationship('itemModel',lazy='dynamic')
#Now we can access itemModel.
    def __init__(self,name):
       self.name=name
       



    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]}



    @classmethod
    def find_by_name(cls, name):
        return storeModel.query.filter_by(name=name).first()  #same as  SELECT* from item WHERE name=name     .first( ) instead of fetchone function



    def save_to_db(self):   #it upserts that means both inserts and updates if already exists so no need for update method.

        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()
