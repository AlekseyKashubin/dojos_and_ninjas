from flask_app.config.mysqlconnection import connectToMySQL





class Dojo:
    DB = 'dojos_and_ninjas_schma'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = """SELECT * FROM dojos;"""
        results = connectToMySQL(cls.DB).query_db(query)
        all_dojos = []
        for dojos in results:
            all_dojos.append( cls(dojos) )
        return all_dojos
    


    @classmethod
    def add_dojo(cls, data):
        query = """
        INSERT INTO dojos (name)
        VALUES ( %(name)s );
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    

    @classmethod
    def get_one(cls,data):
        query = """
        SELECT * FROM dojos
        WHERE dojos.id = %(id)s ;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        one_dojo = cls(results[0])
        return one_dojo

    @classmethod
    def dojo_data(cls,data):
        query = """
        SELECT * FROM dojos
        WHERE id = %(dojo_id)s ;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls (results[0])


    @classmethod
    def delete_dojo(cls,data):
        query = """
        DELETE FROM dojos WHERE id = %(dojo_id)s ;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
