CREATE TABLE e_commerce_transactions (
    transaction_id SERIAL PRIMARY KEY,
    product_id INTEGER,
    product_name VARCHAR(255),
    category VARCHAR(50),
    price DECIMAL(10, 2),
    quantity INTEGER,
    customer_id INTEGER,
    customer_name VARCHAR(255),
    customer_email VARCHAR(255),
    customer_address TEXT,
    transaction_date TIMESTAMP,
    payment_method VARCHAR(50),
    shipping_method VARCHAR(50),
    order_status VARCHAR(50),
    discount_amount DECIMAL(10, 2),
    tax_amount DECIMAL(10, 2),
    total_amount DECIMAL(10, 2),
    coupon_code VARCHAR(20),
    tracking_number VARCHAR(50),
    review_rating INTEGER,
    review_comment TEXT
);