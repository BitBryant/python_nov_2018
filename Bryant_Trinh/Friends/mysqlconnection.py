# a cursor is the object we use to interact with the database
import pymysql.cursors
# Create a class that will give us an object that we can use to connect to a database
class MySQLConnection:
#    def __init__(self, db):
#        connection = pymysql.connect(host = 'localhost',
#                                    user = 'root', # change the user and password as needed
#                                    password = 'root', 
#                                    db = db,
#                                    charset = 'utf8mb4',
#                                    #                                    autocommit = True)
        # establish the connection to the database
#        self.connection = connection
    # to query the database, we will use this method, which needs a query and possibly some data
    def __init__(self, db):
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db=db,
                                    charset='utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        print("initialize")
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # if the query is an insert, return the id of the last row, since that is the row we just added
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    print("/loasd///")
                    result = cursor.fetchall()
                    return result
                else:
                    # if the query is not an insert or a select, such as an update or delete, commit the changes
                    # return nothing
                    self.connection.commit()
            except Exception as e:
                # in case the query fails
                print("Something went wrong",)
                return False
            finally:
                # close the connection
                self.connection.close()
# this connectToMySQL function creates an instance of MySQLConnection, which will be used by server.py
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)