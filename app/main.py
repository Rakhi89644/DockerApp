from tkinter.messagebox import NO
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi import HTTPException
from db.database import Base,Sessionlocal,engine
from db.models import Users

Base.metadata.create_all(bind=engine) # through this line only we create the table in database 

app = FastAPI()

products = [
    {'product_id':'SKU101','product_name':'KalyanJwell','quantity':1,'currency':'$','price':10000},
    {'product_id':'SKU102','product_name':'KalyanDiamond','quantity':2,'currency':'Euro','price':20000},
    {'product_id':'SKU103','product_name':'KalyanGold','quantity':2,'currency':'$','price':30000},
    {'product_id':'SKU104','product_name':'vistara','quantity':4,'currency':'$','price':40000}
]

# @app.get('/products')

# def user_list():
#     return{'products':products}

# adding filter to the userlist to accept min and max parameter
@app.get('/products')

def user_list(min:Optional[int]=None,max:Optional[int]=None):

    if min and max:
        filter_products =list(
            filter(lambda product: max>= products['price'] >=min,products)
        )
        return{'products':filter_products}
        return{'products':products}
# check the product if the request user exits in the database
@app.get('/products_check')
def product_check(product_id):

    if not products[product_id]:
        raise HTTPException(status_code=404,detail='product not found')


@app.get('/products/{product_id}')
def user_detail(product_id):
    product_check(product_id)
    return {'product': products[product_id]}

# add class from basemodel to add one new product 
class product(BaseModel):
    product_id: int
    product_name:str


    
@app.post('/products')
def user_add(products:product):
    products.append(product)
    return{'product':product[-1]}