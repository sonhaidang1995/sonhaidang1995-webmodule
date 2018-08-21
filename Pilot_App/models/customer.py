from mongoengine import *

class Customer(Document):
    name = StringField()
    gender = IntField()
    emailz = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()