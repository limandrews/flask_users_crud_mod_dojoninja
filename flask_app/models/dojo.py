# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the dojo table from our database
from pprint import pprint
from flask_app.models.ninja import Ninja

DATABASE = "dojos_and_ninjas"
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # Create 
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)



    # read/retrieve
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append( Dojo(dojo) )
        return dojos

# retrieve one
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(result[0])
        return dojo


    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id=ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        dojo = Dojo(results[0])
        for result in results:
            ninja_dict = {
                'id': result['ninjas.id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'age': result['age'],
                'dojo_id': result['dojo_id'],
                'created_at': result['ninjas.created_at'],
                'updated_at': result['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_dict))
        return dojo 


    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name = %(name)s WHERE id= %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result 

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def show_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninja ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        for result in results:
            ninja_dict = {'id': result['ninjas.id'], 'first_name': result['first_name'], 'last_name': result['last_name'], 'dojo_id': result['dojo_id'], 'created_at': result['ninjas.created_at'], 'updated_at': result['ninjas.updated_at']}
        # return Dojo(result[0])