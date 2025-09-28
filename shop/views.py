import flask
from .models import Product
import os
import dotenv
import requests


def render_catalog():
    list_products = Product.query.all()
    
    if flask.request.method == "POST":
        category = flask.request.form["category"]
        if category != "all":
            list_products = Product.query.filter_by(category = category)
    return flask.render_template('catalog.html', list_products = list_products)

#
PATH_ENV = os.path.abspath(os.path.join(__file__, "..", "..", ".env"))
#
dotenv.load_dotenv(dotenv_path=PATH_ENV)

#
API_URL_MONOBANK = 'https://api.monobank.ua/api/merchant/invoice/create'
#
TOKEN_MONOBANK = os.environ['TOKEN_MONOBANK']


def create_payment():
    ''''''

    #
    product_id =flask.request.args.get(key='productId')
    #
    product = Product.query.get(int(product_id))
    #
    price = int(product.price) * 100
    
    #
    payload= {
        "amount": price,#
        "ccy": 980,#
        "redirectUrl": "http://127.0.0.1:5000/"#
    }

    #
    headers = {"X-Token": TOKEN_MONOBANK}

    #
    response = requests.post(API_URL_MONOBANK, json = payload, headers = headers)

    #
    payment_form_url = response.json()["pageUrl"]

    #
    return flask.redirect(payment_form_url)
