
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from datetime import date
import mysql.connector
import os
from mysql.connector import Error
from model.Inventory import InventoryUpdate;

app = FastAPI()



try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ecommerce_db"
    )
    cursor = db.cursor(dictionary=True)
    print("Connection successfull",cursor)
except Error as e:
    print("Connection not successfull")


# End Points
@app.get("/inventory")
def get_inventory():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

@app.post("/inventory/update")
def update_inventory(data: InventoryUpdate):
    cursor.execute("UPDATE products SET stock = %s WHERE id = %s", (data.new_stock, data.product_id))
    db.commit()
    return {"message": "Inventory updated"}


@app.get("/inventory/low-stock")
def low_stock():
    cursor.execute("SELECT * FROM products WHERE stock < 10")
    return cursor.fetchall()