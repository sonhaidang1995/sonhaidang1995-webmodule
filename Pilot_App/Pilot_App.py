from flask import *
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
        gender = g
        )    
    return render_template('search.html', 
    all_service = all_service
    )
# square
@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer = all_customer)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template(
        'admin.html', 
        all_service = all_service
    )

@app.route('/customer/<int:g>/')
def t_customer(g):
    all_t_customer = Customer.objects[:10](
        gender = g,
        contacted = False
    )
    return render_template('t_customer.html', all_t_customer = all_t_customer, g = g)

@app.route('/delete/<service_id>')
def delete(service_id):
    delete_service = Service.objects.with_id(service_id)
    if delete_service is not None:
        delete_service.delete()
        return redirect(url_for('admin'))
    else:
        return "Not found"

@app.route('/new-service',methods = ["GET","POST"])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']
        new_service = Service(
            name = name,
            yob = yob,
            phone = phone,
            gender = gender
        )
        new_service.save()
        return redirect(url_for('admin'))   
    
@app.route('/detail/<service_id>')
def detail(service_id):
    profile = Service.objects.with_id(service_id)
    if profile is not None:
        return render_template('detail.html',profile = profile)
    else:
        return "Not found"

@app.route('/update-service/<service_id>', methods = ["GET","POST"])
def update(service_id):
    u_profile = Service.objects.with_id(service_id)
    if request.method == "GET":
        if u_profile is not None:
            return render_template('update.html',u_profile = u_profile)
        else:
            return "Not found"
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']
        height = form['height']
        address = form['address']
        Service.objects.with_id(service_id).update(
            name = name,
            yob = yob,
            phone = phone,
            gender = gender,
            height = height,
            address = address
        )
        return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
 