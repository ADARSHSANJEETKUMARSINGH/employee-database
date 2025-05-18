import mysql.connector

# Pehle se kisi specific database se connect mat karo
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123Andhapaisa@"
    # database yahan mention nahi karna
)

cursor = conn.cursor()

# Ab database create karo
cursor.execute("CREATE DATABASE company")
print("Database created successfully.")

cursor.close()
conn.close()
