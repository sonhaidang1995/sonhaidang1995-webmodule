from models.service import Service
import mlab
from faker import Faker
from random import randint,choice
mlab.connect()

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
        status = choice([True, False])
    )

    new_service.save()
