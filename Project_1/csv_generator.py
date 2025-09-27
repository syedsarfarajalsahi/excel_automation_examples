import pandas as pd
import random
from faker import Faker

fake = Faker()

# Sample products
products = ["Pen", "Notebook", "Pencil", "Eraser", "Marker", "Highlighter"]

data = []
for _ in range(1000):
    # Random date format
    date_format = random.choice(["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"])
    date = fake.date_between(start_date='-30d', end_date='today').strftime(date_format)

    # Random product
    product = random.choice(products)

    # Random quantity with some missing values
    quantity = random.choice([random.randint(1, 20), None])

    # Random amount with some missing values
    amount = None if random.random() < 0.05 else quantity * random.randint(10, 50) if quantity else None

    data.append([date, product, quantity, amount])

# Create DataFrame
df = pd.DataFrame(data, columns=["Date", "Product", "Quantity", "Amount"])

# Save to CSV
df.to_csv("raw_sales_1000.csv", index=False)
print("raw_sales_1000.csv generated with 1000 rows!")
