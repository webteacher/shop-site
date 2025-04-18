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
        self.connect()
        self.cursor.execute('''SELECT * FROM categories ''')
        categories = self.cursor.fetchall()
        self.connection.close()

        return categories
    
    def get_items_by_category_id(self, category_id):
        self.connect()


        self.cursor.execute('''SELECT * FROM items WHERE category_id = ? ''', [category_id])
        items = self.cursor.fetchall()
        self.connection.close()

        return items
    
    def get_item(self,item_id):
        self.connect()

        self.cursor.execute('''SELECT i.id, i.name, i.description, i.price, c.name, i.category_id, i.image
                             FROM items i
                            INNER JOIN categories c ON i.category_id = c.id                          
                             WHERE i.id = ? ''', [item_id])

        item = self.cursor.fetchone()
        self.connection.close()

        return item
    
    def create_order(self):
        self.connect()

        self.cursor.execute ('''INSERT INTO orders(status)
                             VALUES(?)''', ['new'])
        self.connection.commit()
        order_id = self.cursor.lastrowid
        self.connection.close()

        return order_id

    def add_item_in_order(self, item_id,order_id):
        self.connect()
        self.cursor.execute('''SELECT * FROM items_in_orders
         WHERE (item_id =? AND order_id =?)''', [item_id,order_id])
        item  = self.cursor.fetchone()
        if item :
            self.cursor.execute('''UPDATE items_in_orders
            SET quantity  = ?
            WHERE (item_id =? AND order_id =?) ''', [item[3] + 1 ,item_id, order_id])
        else :
            self.cursor.execute(''' INSERT INTO items_in_orders(order_id,item_id)
                                VALUES (?,?)''', [ order_id,item_id])

        self.connection.commit()
        self.connection.close()

    

    def update_order(self,full_name,phone_number,address,payment_type,city,order_id,price_total):
        self.connect()

        self.cursor.execute('''UPDATE orders
                            SET full_name = ?,phone_number = ?,address = ?,payment_type = ? ,city = ?,price_total = ?
                            WHERE id  = ?
                             ''',[full_name,phone_number,address,payment_type,city,order_id,price_total])
        self.connection.commit()
        self.connection.close()


    def search_items (self, search):
        self.connect()


        self.cursor.execute('''SELECT * FROM items WHERE name LIKE ? ''', ["%"+search+"%"])
        items = self.cursor.fetchall()
        self.connection.close()

        return items

    def get_order_items(self, order_id): 
        self.connect()
        self.cursor.execute('''SELECT  io.id, i.name, i.price, i.image, io.quantity
        FROM items_in_orders io
        INNER JOIN items i ON io.item_id = i.id 
        WHERE io.order_id = ?''',[int(order_id)])
        items = self.cursor.fetchall()
        self.connection.close()
        return items

    def delete_item_in_order(self, item_in_order_id):
        self.connect()
        self.cursor.execute('''DELETE FROM items_in_orders
                                WHERE id = ?''',[item_in_order_id])
        self.connection.commit()
        self.connection.close()

                

        







     
     

    
        