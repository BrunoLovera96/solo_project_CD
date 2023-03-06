from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Chore:
    schema = "solo_project"
    def __init__(self,data):
        self.idChores = data['idChores']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data ['created_at']
        self.finished_at = data ['finished_at']
        self.finished = data['finished']
        self.product_id = data['product_id']

    @classmethod
    def save_chore(cls,data):
        query = """INSERT INTO chores (name, description, created_at, finished, product_id, user_id) 
        VALUES (%(name)s, %(description)s, NOW(), 0, %(product_id)s, %(user_id)s);"""
        results = connectToMySQL(cls.schema).query_db(query, data)
        # print('>>>>>>>>>>>>>>>>>>', results)
        return results

    @classmethod
    def chores_pending(cls, data):
        query = "SELECT * FROM chores WHERE user_id = %(id)s AND finished = 0;"
        users_with_products_and_chores = connectToMySQL(cls.schema).query_db(query,data)
        # print('>>>>>>>>>>>>>>>>>> ESTO ES SOLO ROMI', users_with_products_and_chores)
        return users_with_products_and_chores

    @classmethod
    def chores_pending_with_product(cls, data):
        query = "SELECT * FROM chores c LEFT JOIN products p ON c.product_id = p.idProducts WHERE c.user_id = %(id)s AND c.finished = 0 ORDER BY c.created_at DESC;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        # print('>>>>>>>>>>>>>>>>>> ESTO ES SOLO ROMI', users_with_products_and_chores)
        return results

    @classmethod
    def chores_finished(cls, data):
        query = "SELECT *  FROM chores WHERE user_id = %(id)s AND finished = 1;"
        users_with_products_and_chores = connectToMySQL(cls.schema).query_db(query,data)
        # print('>>>>>>>>>>>>>>>>>> ESTO ES SOLO ROMI', users_with_products_and_chores)
        return users_with_products_and_chores

    @classmethod
    def chores_finished_with_product(cls, data):
        query = "SELECT * FROM chores c LEFT JOIN products p ON c.product_id = p.idProducts WHERE c.user_id = %(id)s AND c.finished = 1 ORDER BY c.finished_at DESC LIMIT 10;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        # print('>>>>>>>>>>>>>>>>>> ESTO ES SOLO ROMI', users_with_products_and_chores)
        return results


    @classmethod
    def finish_chore(cls,data):
        query = "UPDATE chores SET finished = 1, finished_at = NOW() WHERE idChores = %(idChores)s"
        results = connectToMySQL(cls.schema).query_db(query,data)
        return results

    @classmethod
    def unfinish_chore(cls,data):
        query = "UPDATE chores SET finished = 0 WHERE idChores = %(idChores)s"
        results = connectToMySQL(cls.schema).query_db(query,data)
        return results

    @classmethod
    def get_one(cls,data):
        query = "SELECT idProducts, title, description, price, quantity, paints.created_at, paints.updated_at, user_id FROM users JOIN paints ON idUsers = user_id WHERE idPaints = %(idPaints)s;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        return ( results[0] )

