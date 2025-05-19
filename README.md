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



## API Endpoints

### Product Management

- **POST /products**
  Add a new product to inventory.
  ```json
  {
    "name": "Laptop",
    "category": "Electronics",
    "price": 1200.0,
    "stock": 20
  }
  ```

- **GET /inventory**
  Retrieve the current list of products.

- **POST /inventory/update**
  Update the stock level of a product.
  ```json
  {
    "product_id": 1,
    "new_stock": 15
  }
  ```

- **GET /inventory/low-stock**
  List products with stock less than 10.

### Sales and Revenue

- **POST /sales**
  Retrieve sales data by date range or product ID.
  ```json
  {
    "start_date": "2025-05-01",
    "end_date": "2025-05-03",
    "product_id": 2
  }
  ```

- **GET /revenue/{period}**
  Get revenue grouped by:
  - `daily`
  - `weekly`
  - `monthly`
  - `annual`

  Example:
  `GET /revenue/daily`



## Database Schema Documentation

### 1. `products` Table
- **Purpose**: Stores the list of all products available in the store.
- **Fields**:
  - `id` (INT, PK, AUTO_INCREMENT): Unique identifier for the product.
  - `name` (VARCHAR): Name of the product.
  - `category` (VARCHAR): Category to which the product belongs.
  - `price` (FLOAT): Price per unit of the product.
  - `stock` (INT): Current stock available in inventory.

### 2. `sales` Table
- **Purpose**: Tracks sales transactions for products.
- **Fields**:
  - `id` (INT, PK, AUTO_INCREMENT): Unique identifier for each sale.
  - `product_id` (INT, FK → products.id): Refers to the product sold.
  - `quantity` (INT): Number of units sold.
  - `amount` (FLOAT): Total sale amount.
  - `date` (DATE): Date the sale occurred.

### Relationships
- `sales.product_id` references `products.id`. This establishes a **foreign key relationship**, ensuring each sale is linked to a valid product.

### Indexing
- Primary keys are automatically indexed.
- You may add indexes on:
  - `sales.date` for faster revenue queries.
  - `products.category` for category-based filtering.


