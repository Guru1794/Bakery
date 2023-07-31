from flask import Flask,request
import sqlite3

app=Flask(__name__)

con=sqlite3.connect("db.db")
con.execute("CREATE TABLE IF NOT EXISTS cake(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(20),email VARCHAR(20), message VARCHAR(70))");
con.commit()
con.close()

@app.get("/form")
def formg():
    con=sqlite3.connect("db.db")   
    cur=con.cursor()
    cur.execute("SELECT * FROM cake ")
    op=cur.fetchall()
    con.close()
    return op

@app.post("/form")
def formp():
    
    name=request.form.get("name")
    email=request.form.get("email")
    message=request.form.get("message")
    
    con=sqlite3.connect("db.db")
    cur=con.cursor()
    cur.execute("INSERT  INTO cake  (name,email,message) VALUES(?,?,?)",(name,email,message))
    con.commit()
    con.close()
    
    return "inserted"

if(__name__=="__main__"):
    app.run(debug=True)