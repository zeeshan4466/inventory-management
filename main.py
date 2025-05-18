
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from datetime import date
import mysql.connector
import os
from mysql.connector import Error

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

