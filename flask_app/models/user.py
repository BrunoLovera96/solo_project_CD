from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.product import Product
# from flask_app.models.chore import Chore
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class User:
    schema = "solo_project"
    def __init__(self,data):
        self.idUsers = data['idUsers']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.company = data ['company']
        self.department = data ['department']
        self.position = data['position']
        self.email = data['email']
        self.password = data['password']
        self.available = data['available']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name,last_name,email,password,created_at, updated_at, company, department, position) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s, NOW(), NOW(), %(company)s, %(department)s, %(position)s);"
        return connectToMySQL(cls.schema).query_db(query,data)

    # @classmethod
    # def get_users_with_products(cls):
    #     query = "SELECT * FROM users u LEFT JOIN users_has_products uhp ON u.idUsers = uhp.users_idUsers LEFT JOIN products p ON p.idProducts = uhp.users_idUsers;"
    #     users_with_products = connectToMySQL(cls.schema).query_db(query)
    #     return users_with_products

    @classmethod
    def get_users_with_products_and_chores(cls, data):
        query = "SELECT * FROM users u LEFT JOIN products p ON p.user_id = u.idUsers LEFT JOIN chores c ON c.product_id = p.idProducts WHERE idUsers = %(id)s;"
        users_with_products_and_chores = connectToMySQL(cls.schema).query_db(query,data)
        # print('>>>>>>>>>>>>>>>>>> ESTO ES SOLO ROMI', users_with_products_and_chores)
        return users_with_products_and_chores

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE idUsers = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        # print('>>>>>>>>>>>>>>>>>> ESTO ES USER', results[0].first_name)
        return results


    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE idUsers = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        return cls(results[0])

    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, position = %(position)s, company = %(company)s, department = %(department)s, email = %(email)s WHERE idUsers = %(idUsers)s;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        return results

    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.schema).query_db(query,user)
        if len(results) >=1:
            flash("El email ya se encuentra registrado", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Correo invalido", "register")
            is_valid = False
        if len(user['first_name']) < 3:
            flash("El nombre del usuario debe tener al menos 3 caracteres", "register")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("El apellido del usuario debe tener al menenos 3 caracteres", "register")
            is_valid = False
        if len(user['password']) < 8:
            flash("La contraseña debe tener como mínimo 8 caracteres", "register")
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Las contraseñas ingresadas no coinciden", "register")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_Valid = True
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(User.schema).query_db(query,user)
        if not EMAIL_REGEX.match(user['email']):
            flash("Email inválido!", "register")
            is_valid = False
        return is_valid