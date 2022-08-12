from flask import Flask, render_template
import sqlite3
import conf


app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect(conf.DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn



@app.route("/")
@app.route("/data")
def home():
    data =[
        (33,"2022-08-08 15:27:04.304805"),
        (34,"2022-08-08 15:27:06.312951"),
        (34,"2022-08-08 15:27:07.316567"),
        (31,"2022-08-08 15:27:05.309154"),
        (33,"2022-08-08 15:27:14.306878"),
        (34,"2022-08-08 15:27:15.315668"),
        (33,"2022-08-08 15:27:16.318544"),
        (34,"2022-08-08 15:27:17.321504"),
        (34,"2022-08-08 15:27:18.324426"),
        (35,"2022-08-08 15:27:19.327738"),
        (35,"2022-08-08 15:27:20.332217"),
        (32,"2022-08-08 15:27:21.335769"),
        (33,"2022-08-08 15:27:22.338870")
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("line_chart.html", data=data, labels=labels, values=values)

if __name__ == '__main__':
    app.run()