from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Product:
    schema = "solo_project"
    def __init__(self,data):
        self.idProducts = data['idProducts']
        self.title = data['title']
        self.description = data['description']
        self.project = data['project']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.date_start = data['date_start']
        self.date_finished = data['date_finished']
        self.deadline = data['deadline']
        self.finished = data['finished']

    @classmethod
    def save_product(cls,data):
        query = """INSERT INTO products (title, description, project, created_at, updated_at, date_start, deadline, finished, user_id) 
        VALUES (%(title)s, %(description)s, %(project)s, NOW(), NOW(), %(date_start)s, %(deadline)s, 0, %(user_id)s);"""
        results = connectToMySQL(cls.schema).query_db(query, data)
        # print('>>>>>>>>>>>>>>>>>>', results)
        return results

    @classmethod
    def product_pending(cls, data):
        query = "SELECT * FROM products WHERE user_id = %(id)s AND finished = 0 ORDER BY deadline DESC;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        # print('>>>>>>>>>>>>>>>>>> ESTO productos pendientes', results)
        return results

    @classmethod
    def product_finished(cls, data):
        query = "SELECT * FROM products WHERE user_id = %(id)s AND finished = 1;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        # print('>>>>>>>>>>>>>>>>>> ESTO ES SOLO ROMI', users_with_products_and_chores)
        return results

    @classmethod
    def finish_product(cls,data):
        query = "UPDATE products SET finished = 1, date_finished = NOW() WHERE idProducts = %(idProducts)s"
        results = connectToMySQL(cls.schema).query_db(query,data)
        return results

    @classmethod
    def unfinish_product(cls,data):
        query = "UPDATE products SET finished = 0 WHERE idProducts = %(idProducts)s"
        results = connectToMySQL(cls.schema).query_db(query,data)
        return results

    @classmethod
    def get_product_by_id(cls,data):
        query = "SELECT * FROM products WHERE idProducts = %(idProducts)s"
        results = connectToMySQL(cls.schema).query_db(query,data)
        return results

    @classmethod
    def get_chores_pending_from_product(cls,data):
        query = "SELECT * FROM products p LEFT JOIN chores c ON c.product_id = p.idProducts WHERE p.idProducts = %(idProducts)s AND c.finished = 0;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        # print('>>>>>>>>>>>>>>>>>> ESTO ES SOLO get_chores_pending_from_product', results)
        return results

    @classmethod
    def get_chores_finished_from_product(cls,data):
        query = "SELECT * FROM products p LEFT JOIN chores c ON c.product_id = p.idProducts WHERE idProducts = %(idProducts)s AND c.finished = 1;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        # print('>>>>>>>>>>>>>>>>>> ESTO ES SOLO ROMI', users_with_products_and_chores)
        return results
    
