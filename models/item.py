import sqlite3
from db import db


class itemModel(db.Model):

    __tablename__='item'
    id=db.Column(db.Integer,primary_key=True)
    price=db.Column(db.Float(precision=2))
    name=db.Column(db.String(80))
    store_id=db.Column(db.Integer,db.ForeignKey('stores.id'))
    store=db.relationship('storeModel')
#ForeignKey refers to id from a different table. Now store_id is linked with the other tables id. Now we can not delete a store untill all items are deleted in that store.
    def __init__(self,name,price,store_id):
       self.name=name
       self.price=price
       self.store_id=store_id


    def json(self):
        return {'name':self.name,'price':self.price}



    @classmethod
    def find_by_name(cls, name):
        return itemModel.query.filter_by(name=name).first()  #same as  SELECT* from item WHERE name=name     .first( ) instead of fetchone function



    def save_to_db(self):   #it upserts that means both inserts and updates if already exists so no need for update method.

        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()




