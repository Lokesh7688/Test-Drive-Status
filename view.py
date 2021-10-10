@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        customer_id = request.form['customer_id']
        name = request.form['name']
        age = request.form['age']
        status = request.form['status']
        customer = customerModel(
            customer_id=customer_id, name=name, age=age, status=status)
        db.session.add(customer)
        db.session.commit()
        return redirect('/data')
