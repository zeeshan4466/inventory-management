-- Insert categories
INSERT INTO categories (name) VALUES ('Electronics'), ('Groceries'), ('Clothing');

-- Insert products
INSERT INTO products (name, category_id, price, stock)
VALUES
('Smartphone', 1, 699.99, 50),
('Laptop', 1, 999.00, 30),
('Apples (1kg)', 2, 3.50, 100),
('T-shirt', 3, 15.00, 200);

-- Insert sales (simulate a few days of sales)
INSERT INTO sales (product_id, quantity, amount, date)
VALUES
(1, 2, 1399.98, '2025-05-01'),
(3, 5, 17.50, '2025-05-02'),
(2, 1, 999.00, '2025-05-02'),
(4, 3, 45.00, '2025-05-03'),
(3, 10, 35.00, '2025-05-03');

-- Insert inventory logs
INSERT INTO inventory_logs (product_id, old_stock, new_stock)
VALUES
(1, 60, 50),
(2, 35, 30),
(3, 110, 100),
(4, 210, 200);
