import sqlite3

class DatabaseManager ():
    
    def __init__(self):
        self.connection  = None
        self.cursor = None
    
    def connect(self):
        self.connection  = sqlite3.connect("shop.db")
        self.cursor = self.connection.cursor()

    def get_all_items(self):
        self.connect()
        self.cursor.execute('''SELECT * FROM items ''')
        items = self.cursor.fetchall()
        self.connection.close()
        return items

    def get_all_categories(self):
        self.cursor.execute('''SELECT * FROM categories ''')
        categories = self.cursor.fetchall()
        return categories
    
    def get_items_by_category_id(self, category_id):
        self.cursor.execute('''SELECT * FROM items WHERE category_id = ? ''', [category_id])
        items = self.cursor.fetchall()
        return items
    
    def get_item(self,item_id):
        self.cursor.execute('''SELECT i.id, i.name, i.description, i.price, c.name, i.category_id, i.image
                             FROM items i
                            INNER JOIN categories c ON i.category_id = c.id                          
                             WHERE i.id = ? ''', [item_id])

        item = self.cursor.fetchone()
        return item
    
    def create_order(self):
        self.cursor.execute ('''INSERT INTO orders(full_name)
                             VALUES("")''')
        self.connection.commit()
        order_id = self.cursor.lastrowid
        return order_id

    def add_item_in_order(self, item_id,order_id,quantity):
        self.cursor.execute(''' INSERT INTO items_in_orders(order_id,item_id,quantity)
                            VALUES (?,?,?)''', [ order_id,item_id,quantity])
        self.connection.commit()
    

    def update_order(self,full_name,phone_number,address,payment_type,city,order_id,price_total):
        self.cursor.execute('''UPDATE orders
                            SET full_name = ?,phone_number = ?,address = ?,payment_type = ? ,city = ?,price_total = ?
                            WHERE id  = ?
                             ''',[full_name,phone_number,address,payment_type,city,order_id,price_total])
        self.connection.commit()
        







     
     

    
        