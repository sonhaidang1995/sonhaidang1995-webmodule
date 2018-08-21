from flask import Flask, render_template
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer
# import populate

app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    # all_service = Service.objects(
    #     gender = g, 
    #     yob__lte = 1998, 
    #     height__gt = 165)
    all_service = Service.objects(
        gender = g, 
        address__icontains = 'Square')    
    return render_template('search.html', 
    all_service = all_service
    )
# square
@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer = all_customer)

@app.route('/customer/<int:g>/')
def t_customer(g):
    all_t_customer = Customer.objects[:10](
        gender = g,
        contacted = False
    )
    return render_template('t_customer.html', all_t_customer = all_t_customer, g = g)

if __name__ == '__main__':
    app.run(debug=True)
 