from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = 'users' # make a variable to use in the result variable that uses the database's name instead of typing out 'users' each time

    def __init__(self, data): # constructor method to make the database key info to be accessable by the templates
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls): # this is a method to get all of the information from each table about a user
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for i in results:
            users.append(cls(i)) # this combines all the table info into one list
        return users

    @classmethod
    def save(cls, data): #this is a method to save a new users information into our database
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);" # inserts new key values from the form into our database
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data): # this method specifically gets one user based on their id key
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0]) # returns the results that are on the index of 0

    @classmethod
    def update(cls, data): # this method is what updates a current users info to whatever info is submitted through the form
        query = """UPDATE users SET 
        first_name=%(first_name)s,
        last_name=%(last_name)s,
        email=%(email)s, 
        updated_at= NOW()
        WHERE id = %(id)s""" # lines 38-42 replaces the old user info with the new given info based on each key 
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy(cls, data): # this method deletes a selected user
        query = """ DELETE FROM users 
        WHERE id = %(id)s""" #this deletes the users table data from the database
        return connectToMySQL(cls.db).query_db(query, data)