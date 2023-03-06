from flask_app.controllers.users import User
from flask_app.controllers.products import Product
from flask_app.controllers.chores import Chore
from flask_app import app

if __name__ == '__main__':
    app.run(debug=True)