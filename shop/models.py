from project.db import DATABASE


class Product(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String(50))
    price = DATABASE.Column(DATABASE.Float)
    category = DATABASE.Column(DATABASE.String(50))