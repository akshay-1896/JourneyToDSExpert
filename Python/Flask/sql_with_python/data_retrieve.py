import mysql.connector as mc

user_credentials = {
    "host": "localhost",
    "username": "root", 
    "password": r"@b2h8a1r18a1t20",
    "database": "flaskapp"}
conn = mc.connect(**user_credentials)

query = "SELECT * FROM contactdata"

try:
    # my_curs = conn.cursor(buffered=True) # buffered=True is used to store the data in the buffer memory and it is used to fetch the data
    # cursor object is used to interact with the database and it is a temporary work area created in the system memory when a SQL statement is executed
    my_curs = conn.cursor()
    my_curs.execute(query)

    # rows = my_curs.fetchmany(2) # fetchmany fetches more than one row from the cursor and the number of rows to fetch is specified in the fetchmany() method
    data = my_curs.fetchall() # fetchall is used to fetch all the data from the cursor
    print(data)
    print("Data Fetched")
    
except Exception as e:
    print("Unable to fetch data: ", e)  

my_curs.close() # if cursor is not closed, it will consume the memory and if cursor is closed without fetching the data, it will give an error, for this to prevent error we use buffered=True
conn.close()

