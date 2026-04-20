from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

DB = "employees.db"


def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    employees = cur.fetchall()
    conn.close()
    return render_template("index.html", employees=employees)


@app.route("/employees", methods=["POST"])
def add_employee():
    name = request.form["name"]

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("INSERT INTO employees(name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/employees", methods=["GET"])
def get_employees():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    conn.close()

    return jsonify(rows)


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
