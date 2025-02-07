from flask import Flask,render_template
from db_scripts import DatabaseManager

app = Flask(__name__)
db = DatabaseManager()

@app.route("/")
def index():
    all_items = db.get_all_items()
      
    
    return render_template("index.html", items=all_items)




