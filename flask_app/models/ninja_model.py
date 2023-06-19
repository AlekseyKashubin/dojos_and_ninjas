from flask_app.config.mysqlconnection import connectToMySQL






class Ninja:
    DB = 'dojos_and_ninjas_schma'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']


    @classmethod
    def get_all(cls, data):
        query = """SELECT * FROM ninjas
        WHERE dojo_id = %(id)s ;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas



    @classmethod
    def add_ninja(cls, data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    

    @classmethod
    def get_one(cls,data):
        query = """
        SELECT * FROM ninjas
        WHERE id = %(id)s ;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])


    @classmethod
    def update_ninja(cls,data):
        query = """
        UPDATE ninjas
        SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojo_id = %(dojo_id)s 
        WHERE id = %(ninja_id)s ;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results


    @classmethod
    def delete_ninja(cls,data):
        query = """
        DELETE FROM ninjas WHERE id = %(ninja_id)s ;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results


    @classmethod
    def ninja_data(cls,data):
        query = """
        SELECT * FROM ninjas
        WHERE id = %(ninja_id)s ;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls (results[0])

