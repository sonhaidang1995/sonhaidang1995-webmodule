from models.service import Service
import mlab
from faker import Faker
from random import randint,choice
from character import character_random

mlab.connect()

image_list = [
    "../static/image/female-profile.jpg",
    "../static/image/male-profile.jpg",
    "../static/image/night.jpg",
    "../static/image/rocks.jpg",
    "../static/image/lightning.jpg"
]

fake = Faker()
name = fake.name()


# design pattern(MVC, Model+Views+Controller)
# new_service = Service(
#     name = "Quân Kun",
#     yob = 1996,
#     gender = 1,
#     height = 175,
#     phone = "0969111225",
#     address = "Long Biên, Hà Nội",
#     status = False
# )
# new_service.save()
# design pattern(MVC, Model+Views+Controller)
for i in range(50):
    print("Saving service",i+1,"...")
    new_service = Service(
        name = fake.name(),
        yob = randint(1990,2000),
        gender = randint(0,1),
        height = randint(150,190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice([True, False]),
        measurements = [randint(30,90),randint(30,90),randint(30,90)],
        des = character_random(),
        image = choice(image_list)
    )

    new_service.save()
