from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123Andhapaisa@",
    database="company"
)
cursor = conn.cursor()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        post = request.form["post"]
        joining_date = request.form["joining_date"]
        salary = request.form["salary"]

        cursor.execute("INSERT INTO employees (id, name, post, joining_date, salary) VALUES (%s, %s, %s, %s, %s)",
                       (id, name, post, joining_date, salary))
        conn.commit()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)