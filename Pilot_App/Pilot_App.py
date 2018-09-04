from flask import *
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer
from models.account import Account
from models.order import Order
from datetime import datetime
from sent_mail import sent_mail
# import populate

app = Flask(__name__)

app.secret_key = "secret key" 

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
    if 'loggedin' in session:
        if session['loggedin'] == True and session['admin'] == True:
            all_service = Service.objects()
            return render_template(
                'admin.html', 
                all_service = all_service
            )
        else:
            return "Go Home"
    else:
        return "Go Home"

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
        des = form['hobbies']
        measurements = [int(form['round1']),int(form['round2']),int(form['round3'])]
        height = form['height']
        address = form['address']
        status = form['status']
        status1 = False
        if int(status) == 0:
            status1 = True
        elif int(status) == 1:
            status1 = False
        new_service = Service(
            name = name,
            yob = yob,
            phone = phone,
            gender = gender,
            des = des,
            measurements = measurements,
            address = address,
            height= height,
            status = status1
        )
        new_service.save()
        return redirect(url_for('index'))   
    
@app.route('/detail/<service_id>')
def detail(service_id):
    profile = Service.objects.with_id(service_id)
    if 'loggedin' in session:
        if session['loggedin'] == True:
            if profile is not None:
                return render_template('detail.html',profile = profile)
            else:
                return "Not found"
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

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
        des = form['des']
        status = form['status']
        measurements = [int(form['round1']),int(form['round2']),int(form['round3'])]
        status1 = False
        if int(status) == 0:
            status1 = True
        elif int(status) == 1:
            status1 = False
        Service.objects.with_id(service_id).update(
            name = name,
            yob = yob,
            phone = phone,
            gender = gender,
            height = height,
            address = address,
            status = status1,
            des = des,
            measurements = measurements
        )
        return redirect(url_for('admin'))
        # return status

@app.route('/sign-up', methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template('sign-up.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        email = form['email']
        username = form['username']
        password = form['password']

        account = Account(
            name = name,
            email = email,
            username = username,
            password = password
        )
        account.save()
        return redirect(url_for('login'))

@app.route('/login',methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']
    found_user = Account.objects.get(username = username, password = password)
    if username =='admin' and password == 'admin':
        session['loggedin'] = True
        session['admin'] = True
        session['id'] = str(found_user['id'])
        return redirect(url_for('admin'))
    elif found_user is not None:
        session['loggedin'] = True
        session['admin'] = False
        session['id'] = str(found_user['id'])
        return redirect(url_for('index'))
    else:
        return "Invalid username or password"

@app.route('/logout')
def logout():
    session['loggedin'] = False
    return redirect(url_for('login'))

@app.route('/sent/<profile_id>')
def sent(profile_id):
    sent = Order(
        account_id = session['id'],
        service_id = profile_id,
        time = datetime.now(),
        is_accepted = False
    )
    sent.save()
    return render_template('sent.html')

@app.route('/order')
def order():
    id_order = Order.objects()
    return render_template('order.html',id_order = id_order)

@app.route('/approval/<order_id>')
def approval(order_id):
    Order.objects.with_id(order_id).update(
        is_accepted = True
    )
    email = Order.objects.with_id(order_id).account_id['email']
    sent_mail(email)
    return redirect(url_for('order'))

if __name__ == '__main__':
    app.run(debug=True)
 