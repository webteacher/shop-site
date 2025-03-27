from flask import Flask,render_template,request
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

@app.route("/items/<int:item_id>")
def item_page(item_id):
    item = db.get_item(item_id)
    categories = db.get_all_categories()
    return render_template("item_page.html",item = item, categories=categories)


@app.route("/search")
def search_page():
    categories = db.get_all_categories()

    search = request.args.get("search")
    items = db.search_items(search)
    return render_template("search_result.html",items = items, categories=categories)




