
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from datetime import date
import mysql.connector
import os
from mysql.connector import Error
from model.Inventory import InventoryUpdate;
from model.Product import Product;
from model.Sales import SalesQuery;

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

@app.post("/products")
def create_product(product: Product):
    cursor.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (%s, %s, %s, %s)",
        (product.name, product.category, product.price, product.stock)
    )
    db.commit()
    return {"message": "Product created"}

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


@app.post("/sales")
def sales_data(query: SalesQuery):
    conditions = []
    params = []
    if query.start_date:
        conditions.append("date >= %s")
        params.append(query.start_date)
    if query.end_date:
        conditions.append("date <= %s")
        params.append(query.end_date)
    if query.product_id:
        conditions.append("product_id = %s")
        params.append(query.product_id)
    if query.category:
        conditions.append("category = %s")
        params.append(query.category)

    where_clause = " AND ".join(conditions)
    sql = "SELECT * FROM sales" + (f" WHERE {where_clause}" if where_clause else "")
    cursor.execute(sql, tuple(params))
    return cursor.fetchall()


@app.get("/revenue/{period}")
def revenue(period: str):
    if period not in ["daily", "weekly", "monthly", "annual"]:
        raise HTTPException(status_code=400, detail="Invalid period")
    if period == "daily":
        group_by = "DATE(date)"
    elif period == "weekly":
        group_by = "YEARWEEK(date)"
    elif period == "monthly":
        group_by = "DATE_FORMAT(date, '%Y-%m')"
    else:
        group_by = "YEAR(date)"

    cursor.execute(f"SELECT {group_by} as period, SUM(amount) as revenue FROM sales GROUP BY period")
    return cursor.fetchall()