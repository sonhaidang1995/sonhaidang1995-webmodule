from mongoengine import *
from models.customer import Customer
import mlab

mlab.connect()

all_customer = Customer.objects()
for index, customer in enumerate(all_customer,1):
    print("Deleting customer ",index,'...')
    customer.delete()