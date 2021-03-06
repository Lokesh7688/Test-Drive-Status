from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class CustomerModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    status = db.Column(db.String(80))
    
 
    def __init__(self, customer_id,name,age,status):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.status = status
