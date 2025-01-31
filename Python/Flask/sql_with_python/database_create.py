import mysql.connector as mc

conn = mc.connect(host="localhost", username="root", password=r"@b2h8a1r18a1t20", database="flaskapp")

query1 = "Create database flaskapp"
query2 = """Create table contactdata(name varchar(50), age int, roll_no int, email varchar(50), subject varchar(50), message varchar(500))"""
try:
    my_curs = conn.cursor() # cursor object is used to interact with the database
    my_curs.execute(query2) # my_curs.execute is used to execute the query
    conn.commit() # commit is used to save the changes
    print("Table Created")
except Exception as e:
    print("Unable to create table: ", e)
    conn.rollback() # rollback is used to revert the changes


my_curs.close()
conn.close()