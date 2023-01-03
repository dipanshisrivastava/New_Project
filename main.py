from flask import Flask, render_template
# import sqlite3
# con = sqlite3.connect("example.db")
#
# cur = con.cursor()

# cur.execute("CREATE TABLE movie(title, year, score)")
#
# res = cur.execute("SELECT name FROM sqlite_master")

# print(res.fetchone())


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/login')
def login():
    return 'welcome'


if __name__ == '__main__':
    app.run(debug=True)
