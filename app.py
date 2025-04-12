from flask import Flask,render_template,request,session
from db_scripts import DatabaseManager
from flask import request

app = Flask(__name__)
app.config["SECRET_KEY"] = "reve ta stohne dnipr"
db = DatabaseManager()

@app.context_processor
def get_context():
    categories = db.get_all_categories()
    order_id = session.get("order_id", None)
    if order_id:
        order_items  = db.get_order_items(order_id)
    else:
        order_items = []

    return {'categories': categories , 'order_items': order_items }  
    # 

    




@app.route("/")
def index():
    all_items = db.get_all_items()
  


    return render_template("index.html", items=all_items)

@app.route("/categories/<int:category_id>")
def category(category_id):
    category_items = db.get_items_by_category_id(category_id)
  
    return render_template("category.html", items=category_items)

@app.route("/items/<int:item_id>", methods = ["GET", "POST"])
def item_page(item_id):
    item = db.get_item(item_id)
    order_id = session.get("order_id", None)
    if request.method == "POST":
        if not order_id:
            order_id = db.create_order()
            session['order_id' ] = order_id
        db.add_item_in_order(item_id, order_id)
    return render_template("item_page.html",item = item)


@app.route("/search")
def search_page():
    

    search = request.args.get("search")
    items = db.search_items(search)
    return render_template("search_result.html",items = items)

@app.route("/about_us")
def about_us_info():
    

    
    return render_template("info_about_us.html")

@app.route("/contacts")
def contacts():
    
    return render_template("contacts.html")

@app.route("/rules")
def rules():
    
    return render_template("rules.html")






