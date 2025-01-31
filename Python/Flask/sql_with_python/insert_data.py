import mysql.connector as mc

conn = mc.connect(host="localhost", username="root", password=r"@b2h8a1r18a1t20", database="flaskapp")

query = "insert into contactdata(name, age, roll_no, email, subject, message) values('Akshay', 21, 101, 'akshay@upflairs.com', 'Python', 'Hello')"
try:
    my_curs = conn.cursor() # cursor object is used to interact with the database
    my_curs.execute(query) # my_curs.execute is used to execute the query
    conn.commit() # commit is used to save the changes
    print("Data Inserted")
except Exception as e:
    print("Unable to insert data: ", e)
    conn.rollback() # rollback is used to revert the changes


my_curs.close()
conn.close()