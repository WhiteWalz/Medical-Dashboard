from __future__ import annotations
from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float)

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_id(self) -> int:
        return self.id

    def findByID(id) -> Item:
        return Item.query.filter_by(user_id=id).first()
    
    def get_name(self) -> str:
        return self.name
    
    def get_price(self) -> float | None:
        return self.price