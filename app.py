from sqlite3 import Connection

from flask import(Flask, redirect, render_template, request, request_finished, flash,copy_current_request_context)
import sqlite3
import  datetime
data = {
    "home" : {
        "title":"home are",
        "peak time":datetime.datetime.now(),
        "add time":"added now",
    },
        "la": {
            "title": "la area",
            "peak time": datetime.datetime.now(),
            "add time": "added now",

        }
}
app = Flask(__name__)
import sqlite3
"""db: Connection = sqlite3.connect("app.db")""
for db adding
with open("setup.sql","r") as file:
    for line in file.readlines():
        db.executescript(line)
"""
@app.route("/")
def Home():
    return redirect("/blog")
@app.route("/blog")
def main():
    return render_template("index.html",data=data)