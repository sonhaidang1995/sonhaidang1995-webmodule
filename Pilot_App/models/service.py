from mongoengine import *

# Design database
class Service(Document):
# Kế thừa "()"
# Tên collection: chữ cái đầu tiên phải viết hóa (Luật bất thành văn)
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    image = StringField()
    des = StringField()
    measurements = ListField()