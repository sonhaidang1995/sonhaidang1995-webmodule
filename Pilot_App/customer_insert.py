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
from character import character_random
mlab.connect()
fake = Faker()
image_list = [
    "../static/image/female-profile.jpg",
    "../static/image/male-profile.jpg",
    "../static/image/night.jpg",
    "../static/image/rocks.jpg",
    "../static/image/lightning.jpg"
]

for i in range (30):
    print('Saving customer',i+1,'...')
    new_customer = Customer(
        name = fake.name(),
        gender = randint(0,1),
        emailz = fake.email(),
        phone = fake.phone_number(),
        job = fake.job(),
        company = fake.company(),
        contacted = choice([True,False]),
        measurements = [randint(30,90),randint(30,90),randint(30,90)],
        des = character_random(),
        image = choice(image_list)
    )
    new_customer.save()
