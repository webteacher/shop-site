from flask import Flask,render_template
from db_scripts import DatabaseManager

app = Flask(__name__)
db = DatabaseManager()

@app.route("/")
def index():
    all_items = db.get_all_items()
    categories = db.get_all_categories()

    return render_template("index.html", items=all_items, categories=categories)

@app.route("/categories/<int:category_id>")
def category(category_id):
    category_items = db.get_items_by_category_id(category_id)
    categories = db.get_all_categories()
    return render_template("category.html", items=category_items, categories=categories)



