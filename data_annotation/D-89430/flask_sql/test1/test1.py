import sqlite3
from flask import Flask, render_template, request, g

DATABASE = 'your_database.db'

app = Flask(__name__)

# Get a connection to the database (before request)
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Close the database connection (after request)
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Initializes the database (run this separately first)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def bulk_add_data():
    try:
        with app.app_context():
            db = get_db()
            cursor = db.cursor()
            data = [
                (1,'John Doe'),
                (2,'Jane Doe'),
                (3,'Bob Smith')
            ]
            cursor.executemany("""
                INSERT INTO your_table (id, name)
                VALUES (?, ?)
            """, data)
            db.commit()
    except sqlite3.Error as e:
        print(f"Error adding data: {e}")


# Example route to display data from the database
@app.route('/')
def index():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM your_table")  # Replace 'your_table' with your actual table name
    rows = cur.fetchall()
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    # init_db()
    # bulk_add_data()
    app.run(debug=True)