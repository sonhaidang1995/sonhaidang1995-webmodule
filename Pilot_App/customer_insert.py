# Các bước insert dữ liệu vào mlab
# thiết kế cơ sở dữ liệu (import file design)
# import mongoengine
# import chức năng kết nối mlab
# kết nối mlab
# import faker => fake ra các bản ghi vào insert vào mlab

from models.customer import Customer
from mongoengine import *
import mlab
from faker import Faker
from random import randint, choice
mlab.connect()

fake = Faker()

for i in range (50):
    print('Saving customer',i+1,'...')
    new_customer = Customer(
        name = fake.name(),
        gender = randint(0,1),
        emailz = fake.email(),
        phone = fake.phone_number(),
        job = fake.job(),
        company = fake.company(),
        contacted = choice([True,False])
    )
    new_customer.save()
