from flask import Flask, request
from flask_restful import  Api
from flask_jwt import JWT, jwt_required
from resources.user import UserRegister
from security import authenticate, identity
from resources.item import Item,ItemList
import datetime
from models.store import storeModel
from resources.store import Store,StoreList
PORT = 5000
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api = Api(app)
app.secret_key = 'jose'


JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=1800)
}
jwt = JWT(app, authenticate, identity) # /auth endpoint



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister , '/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

@app.before_first_request
def create_tables():
    db.create_all()


if __name__=='__main__':  #so we dont run app accidently while importing anything from app. And only run app when python app.py is explicitly said
    
    from db import db
    db.init_app(app)
    
    app.run(port=PORT, debug=True)
