from flask_restful import Resource
from models.store import storeModel

class Store(Resource):
  def get(self, name):
    store = storeModel.find_by_name(name)
    if store:
      return store.json()
    
    return { 'message': 'Store not found'}, 404

  def post(self, name):
    if storeModel.find_by_name(name):
      return {'message': "A store with the name: {}, already exists".format(name)}, 400

    store = storeModel(name)
    try:
      store.save_to_db()
    except:
      return { 'message': 'An error occured saving your store'}, 500
    
    return store.json(), 201

  def delete(self, name):
    store = storeModel.find_by_name(name)
    if store:
      store.delete()
    
    return { 'message': 'Store deleted' }

class StoreList(Resource):
  def get(self):
    return { 'stores': [ store.json() for store in storeModel.query.all() ] }
