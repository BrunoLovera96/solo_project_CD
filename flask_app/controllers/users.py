from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.product import Product
from flask_app.models.chore import Chore
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/add/user',methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "company": request.form['company'],
        "department": request.form['department'],
        "position": request.form['position'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password']),
    }
    id = User.save_user(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/login/user',methods=['POST', 'GET'])
def login():
    if (request.form.get('email') == '') or (request.form.get('password') == ''):
        flash("Complete the fields!","login")
    else:
        data = {
            'email':request.form.get('email')
        }
        user = User.get_by_email(data)
        if not user:
            flash("Invalid Email","login")
            return redirect('/')
        if not bcrypt.check_password_hash(user.password, request.form['password']):
            flash("Invalid Password","login")
            return redirect('/')
        session['user_id'] = user.idUsers
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    user = User.get_user(data)
    # print('>>>>>>>>>>>>>>>>>> ESTO ES USER', user)

    chores_pending_with_product = Chore.chores_pending_with_product(data)
    chores_finished_with_product = Chore.chores_finished_with_product(data)
    product_pending = Product.product_pending(data)
    # print('>>>>>>>>>>>>>>>>>>', users_with_products_and_chores)
    return render_template("dashboard.html", user=user, chores_pending_with_product=chores_pending_with_product, chores_finished_with_product=chores_finished_with_product, product_pending=product_pending)

@app.route('/show/user')
def show_user():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    user = User.get_user(data)
    product_pending = Product.product_pending(data)
    product_finished = Product.product_finished(data)
    return render_template('show_user.html', user=user, product_pending=product_pending, product_finished=product_finished)

@app.route("/process/update/user", methods = ['POST'])
def updating_user():
    if 'user_id' not in session:
        redirect('/logout')
    data = {
        'idUsers': request.form['idUsers'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'position': request.form['position'],
        'company': request.form['company'],
        'department': request.form['department'],
        'email': request.form['email']
    }
    # print('>>>>>>>>>>>>>>>>>>', data)
    user = User.update_user(data)
    return redirect('/show/user')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
