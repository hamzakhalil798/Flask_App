from flask_restful import Resource,reqparse
from flask_jwt import jwt_required,JWT
import sqlite3
from models.item import itemModel
class Item(Resource):
  # NOTE it is not self.parser, parser belongs to the class not an instance of the clas
  parser = reqparse.RequestParser()
  # We only define price as a parser argument
  # so a user can only set the price of an item:
  parser.add_argument('price', 
    type=float,
    required=True,
    help="This field cannot be left blank")

  parser.add_argument('store_id', 
    type=int,
    required=True,
    help="This field cannot be left blank")

  # @jwt_required(), decorator means the jwt rquest token must be vaild and provided to use this method
  @jwt_required()
  def get(self, name):
    output=itemModel.find_by_name(name)
    if output:
      return output.json()  #itemModel object so we can use the function of itemModel
    else:
      return {'message':'item not found'}

  @jwt_required()
  def post(self, name):
    # if name is found (not None), already exists
    if itemModel.find_by_name(name):
      #or Item.find_by_name   means same
      return { 'message': f"An item with name {name} already exists" }, 400
    
    item = Item.parser.parse_args()

    item = itemModel(name, item['price'],item['store_id'])
    try:
      item.save_to_db()  #as it is now an object of ItemModel so calling the function of ItemModel
    except:
      return {'message': 'An error occurred inserting the item'}, 500
    return item.json(), 201




  @jwt_required()
  def delete(self, name):
    item=itemModel.find_by_name(name)
    if item:
      item.delete()
    return { 'message': "item deleted" }

  @jwt_required()
  def put(self, name):
    data=Item.parser.parse_args()
    item=itemModel.find_by_name(name) #just checks if item present.
    
    if item is None:
      item=itemModel(name,data['price'],data['store_id'])

    else:
      item.price=data['price']
      # return ({'name':updated_item.name,'price':updated_item.price}) same
    
    item.save_to_db()
    return item.json()




class ItemList(Resource):
  def get(self):
    return {'items': [item.json() for item in itemModel.query.all()]}
      
