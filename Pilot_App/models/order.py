from mongoengine import *
from models.service import Service
from models.account import Account

class Order(Document):
    service_id = ReferenceField(Service)
    time = DateTimeField()
    is_accepted = BooleanField()
    account_id = ReferenceField(Account)