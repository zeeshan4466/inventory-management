# E-commerce Admin API

A lightweight backend API built with **FastAPI** and **MySQL** for managing e-commerce dashboards. It supports product management, inventory tracking, and sales/revenue analytics.

---

##  Features

- **Product Management** – Create and list products
- **Sales Reporting** – View sales by date, product, or category
- **Revenue Analysis** – Get revenue stats (daily, weekly, monthly, yearly)
- **Inventory Management** – Monitor stock levels and low-stock alerts
- **Inventory Logs** – Track stock changes over time

---

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: MySQL
- **ORM**: None (uses raw SQL via `mysql-connector-python`)

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/zeeshan4466/ecommerce-admin-api.git
cd ecommerce-admin-api
```
2. **Install dependencies**

```bash
pip install fastapi uvicorn mysql-connector-python
```
3. **Setup MySQL Database**

- Create the database using schema.sql
- Populate with demo_data.sql

```bash
mysql -u root -p < schema.sql
mysql -u root -p ecommerce_db < demo_data.sql
```

4. **Run the API**
```bash
uvicorn main:app --reload
```
