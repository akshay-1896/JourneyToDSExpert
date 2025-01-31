import mysql.connector as mc

conn = mc.connect(host="localhost", username="root", password=r"@b2h8a1r18a1t20")

if conn.is_connected():
    print("Connected")
else:
    print("Not Connected")
    
conn.close()