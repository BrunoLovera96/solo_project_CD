from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.product import Product
from flask_app.models.chore import Chore

@app.route("/process/add/chore", methods = ['POST'])
def adding_chore():
    if 'user_id' not in session:
        redirect('/logout')
    data = {
        'user_id': request.form['user_id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'product_id': request.form['product_id']
    }
    # print('>>>>>>>>>>>>>>>>>>', data)
    chore = Chore.save_chore(data)
    # print('>>>>>>>>>>>>>>>>>>', product)
    return redirect('/dashboard')

@app.route("/process/add/chore/product", methods = ['POST'])
def adding_chore_product():
    if 'user_id' not in session:
        redirect('/logout')
    data = {
        'user_id': request.form['user_id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'product_id': request.form['product_id']
    }
    product_data = {
        'idProducts': request.form['idProducts']
    }
    link = "/show/product/" + product_data['idProducts']
    # print('>>>>>>>>>>>>>>>>>>', link)
    chore = Chore.save_chore(data)
    # print('>>>>>>>>>>>>>>>>>>', product)
    return redirect(link)

@app.route('/process/finish/chore', methods = ['POST'])
def finishing_chore():
    data = {
        'idChores': request.form['idChores']
    }
    Chore.finish_chore(data)
    return redirect ('/dashboard')

@app.route('/process/finish/chore/product', methods = ['POST'])
def finishing_chore_product():
    data = {
        'idChores': request.form['idChores']
    }
    product_data = {
        'idProducts': request.form['idProducts']
    }
    link = "/show/product/" + product_data['idProducts']
    Chore.finish_chore(data)

    return redirect (link)

@app.route('/process/unfinish/chore', methods = ['POST'])
def unfinishing_chore():
    data = {
        'idChores': request.form['idChores']
    }
    Chore.unfinish_chore(data)
    return redirect ('/dashboard')

@app.route('/process/unfinish/chore/product', methods = ['POST'])
def unfinishing_chore_product():
    data = {
        'idChores': request.form['idChores']
    }
    product_data = {
        'idProducts': request.form['idProducts']
    }
    link = "/show/product/" + product_data['idProducts']
    Chore.unfinish_chore(data)

    return redirect (link)