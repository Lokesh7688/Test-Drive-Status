from flask import Flask,render_template,request,redirect
from models import db,CustomerModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        name = request.form['name']
        age = request.form['age']
        status = request.form['status']
        customer = CustomerModel(customer_id=customer_id, name=name, age=age, status = status)
        db.session.add(customer)
        db.session.commit()
        return redirect('/')
 
 
@app.route('/')
def RetrieveList():
    customers = CustomerModel.query.all()
    return render_template('index.html',customers = customers)
 
 
@app.route('/<int:id>')
def Retrievecustomer(id):
    customer = CustomerModel.query.filter_by(customer_id=id).first()
    if customer:
        return render_template('data.html', customer = customer)
    return f"customer with id ={id} Doenst exist"
 
 
@app.route('/<int:id>/update',methods = ['GET','POST'])
def update(id):
    customer = CustomerModel.query.filter_by(customer_id=id).first()
    if request.method == 'POST':
        if customer:
            db.session.delete(customer)
            db.session.commit()
            name = request.form['name']
            age = request.form['age']
            status = request.form['status']
            customer = CustomerModel(customer_id=id, name=name, age=age, status = status)
            db.session.add(customer)
            db.session.commit()
            return redirect('/')
        return f"customer with id = {id} Does nit exist"
 
    return render_template('update.html', customer = customer)
 
 
@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    customer = CustomerModel.query.filter_by(customer_id=id).first()
    if request.method == 'POST':
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return redirect('/')
        abort(404)
 
    return render_template('delete.html')
 
app.run(host='localhost', port=5000, debug=True)