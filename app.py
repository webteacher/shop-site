from flask import Flask,render_template,request,session
from db_scripts import DatabaseManager
from flask import request

app = Flask(__name__)
app.config["SECRET_KEY"] = "reve ta stohne dnipr"
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

@app.route("/items/<int:item_id>", methods = ["GET", "POST"])
def item_page(item_id):
    order_id = session.get("order_id", None)
    item = db.get_item(item_id)
    categories = db.get_all_categories()
    if request.method == "POST":
        if not order_id:
            order_id = db.create_order()
            session['order_id' ] = order_id
        db.add_item_in_order(item_id, order_id)
    return render_template("item_page.html",item = item, categories=categories)


@app.route("/search")
def search_page():
    categories = db.get_all_categories()

    search = request.args.get("search")
    items = db.search_items(search)
    return render_template("search_result.html",items = items, categories=categories)

@app.route("/about_us")
def about_us_info():
    categories = db.get_all_categories()

    
    return render_template("info_about_us.html", categories  = categories)

@app.route("/contacts")
def contacts():
    categories = db.get_all_categories()
    return render_template("contacts.html",categories = categories)

@app.route("/rules")
def rules():
    categories = db.get_all_categories()
    return render_template("rules.html",categories = categories)





