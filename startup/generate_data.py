import psycopg2
from faker import Faker

# Set up a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="som",
    user="som",
    password="som!@#",
    host="127.0.0.1"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a Faker instance
fake = Faker()

# Define the number of rows you want to generate
num_rows = 3000000
batch_size = 1000  # You can adjust the batch size based on your needs

# Generate and insert fake e-commerce transaction data into the PostgreSQL database in batches
for _ in range(0, num_rows, batch_size):
    batch_data = []
    for _ in range(batch_size):
        product_id = fake.random_number(5)
        product_name = fake.word()
        category = fake.random_element(elements=('Electronics', 'Clothing', 'Home & Kitchen', 'Toys', 'Books'))
        price = fake.random_number(2)
        quantity = fake.random_number(2)
        customer_id = fake.random_number(5)
        customer_name = fake.name()
        customer_email = fake.email()
        customer_address = fake.address()
        transaction_date = fake.date_time_this_decade()
        payment_method = fake.random_element(elements=('Credit Card', 'PayPal', 'Bitcoin'))
        shipping_method = fake.random_element(elements=('Standard', 'Express'))
        order_status = fake.random_element(elements=('Processing', 'Shipped', 'Delivered'))
        discount_amount = fake.random_number(2)
        tax_amount = fake.random_number(2)
        total_amount = price * quantity - discount_amount + tax_amount
        coupon_code = fake.word()
        tracking_number = fake.uuid4()
        review_rating = fake.random_number(1, 5)
        review_comment = fake.text()

        batch_data.append((
            product_id, product_name, category, price, quantity, customer_id,
            customer_name, customer_email, customer_address, transaction_date,
            payment_method, shipping_method, order_status, discount_amount, tax_amount,
            total_amount, coupon_code, tracking_number, review_rating, review_comment
        ))

    # Use executemany to insert the batch of data
    cursor.executemany("""
        INSERT INTO e_commerce_transactions (
            product_id, product_name, category, price, quantity, customer_id,
            customer_name, customer_email, customer_address, transaction_date,
            payment_method, shipping_method, order_status, discount_amount, tax_amount,
            total_amount, coupon_code, tracking_number, review_rating, review_comment
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )""", batch_data)

    # Commit the changes to the database
    conn.commit()

# Close the cursor and the database connection
cursor.close()
conn.close()