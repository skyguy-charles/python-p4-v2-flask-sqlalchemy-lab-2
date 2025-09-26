from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates, relationship
from app import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    reviews = relationship("Review", back_populates="customer")
    items = association_proxy("reviews", "item")

    def __repr__(self):
        return f"<Customer {self.id}: {self.name}>"

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    reviews = relationship("Review", back_populates="item")

    def __repr__(self):
        return f"<Item {self.id}: {self.name}>"

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)

    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))

    customer = relationship("Customer", back_populates="reviews")
    item = relationship("Item", back_populates="reviews")

    def __repr__(self):
        return f"<Review {self.id}: {self.comment}>"
























































