from flask_mysqldb import MySQL

database = None

def configure_database(app = None):
    
    global database
    if database:
        return database
    
    if not app:
        raise Exception("You must pass an app to configure_database")
    
    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'extremadura'

    database = MySQL(app)
    
    return database

