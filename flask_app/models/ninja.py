# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the ninja table from our database

DATABASE = "dojos_and_ninjas"
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # Create 
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)



    # read/retrieve
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of ninjas
        ninjas = []
        # Iterate over the db results and create instances of ninjas with cls.
        for ninja in results:
            ninjas.append( Ninja(ninja) )
        return ninjas

# retrieve one
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        ninja = Ninja(result[0])
        return ninja

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id= %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result 

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def show_ninjas(cls, data):
        query = "SELECT dojos.name, ninjas.first_name, ninjas.last_name. ninjas.age FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id"
        result = connectToMySQL(DATABASE).query_db(query, data) 
        return Dojo(result)