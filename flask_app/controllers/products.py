from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.product import Product
from flask_app.models.chore import Chore

@app.route("/process/add/product", methods = ['POST'])
def adding_product():
    if 'user_id' not in session:
        redirect('/logout')
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'project': request.form['project'],
        'date_start': request.form['date_start'],
        'deadline': request.form['deadline'],
        'user_id': request.form['user_id']
    }
    # print('>>>>>>>>>>>>>>>>>>', data)
    product = Product.save_product(data)
    # print('>>>>>>>>>>>>>>>>>>', product)

    return redirect('/dashboard')

@app.route('/process/finish/product', methods = ['POST'])
def finishing_product():
    data = {
        'idProducts': request.form['idProducts']
    }
    Product.finish_product(data)
    return redirect ('/show/products')

@app.route('/process/unfinish/product', methods = ['POST'])
def unfinishing_product():
    data = {
        'idProducts': request.form['idProducts']
    }
    Product.unfinish_product(data)
    return redirect ('/show/user')

@app.route('/show/products')
def show_products():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    user = User.get_users_with_products_and_chores(data)
    product_pending = Product.product_pending(data)
    product_finished = Product.product_finished(data)
    return render_template('show_products.html', user=user, product_pending=product_pending, product_finished=product_finished)

@app.route('/show/product/<int:idProducts>')
def show_product(idProducts):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "idProducts": idProducts
    }
    # print('>>>>>>>>>>>>>>>>>> ESTO ES DATA', data) funciona
    user_data = {
        'id': session['user_id']
    }
    user = User.get_user(user_data)
    chores_pending_from_product = Product.get_chores_pending_from_product(data)
    chores_finished_from_product = Product.get_chores_finished_from_product(data)
    
    # print('>>>>>>>>>>>>>>>>>> ESTO ES chores_from_product', chores_from_product) 

    return render_template('show_product.html', user=user, chores_pending_from_product=chores_pending_from_product, chores_finished_from_product=chores_finished_from_product)


# @app.route('')

