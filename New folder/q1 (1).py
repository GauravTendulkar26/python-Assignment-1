# Sample sales data
sales_data = [
    {"product_name": "Product A", "category": "Category 1", "units_sold": 100, "unit_price": 20.5},
    {"product_name": "Product B", "category": "Category 1", "units_sold": 150, "unit_price": 15.0},
    {"product_name": "Product C", "category": "Category 2", "units_sold": 200, "unit_price": 25.0},
    {"product_name": "Product D", "category": "Category 2", "units_sold": 50, "unit_price": 30.0},
    {"product_name": "Product E", "category": "Category 3", "units_sold": 300, "unit_price": 10.0},
]

# Function to calculate total sales
def calculate_total_sales(data):
    """To find total sales"""
    total_sales = 0
    for item in data:
        total_sales += item["units_sold"] * item["unit_price"]
    return total_sales

# Function to calculate average sales per product
def calculate_average_sales(data):
    """To find average sales per product"""
    total_sales = calculate_total_sales(data)
    total_products = len(data)
    return total_sales / total_products if total_products > 0 else 0

# Function to find top-selling products
def find_top_selling_products(data):
    top_product = 0
    for product in data:
        if product["units_sold"]>top_product: top_product = product["units_sold"]
    return top_product["product_name"], top_product["units_sold"]

# Function to calculate sales by category
def calculate_sales_by_category(data):
    category_sales = {}
    for item in data:
        category = item["category"]
        sales = item["units_sold"] * item["unit_price"]
        if category in category_sales:
            category_sales[category] += sales
        else:
            category_sales[category] = sales
    return category_sales

# Running the analysis
total_sales = calculate_total_sales(sales_data)
average_sales = calculate_average_sales(sales_data)
top_product, top_units = find_top_selling_products(sales_data)
sales_by_category = calculate_sales_by_category(sales_data)

# Printing the results
print(f"Total Sales: Rs{total_sales:.2f}")
print(f"Average Sales per Product: Rs{average_sales:.2f}")
print(f"Top Selling Product: {top_product} ({top_units} units sold)")
print("Sales by Category:")
for category, sales in sales_by_category.items():
    print(f"  {category}: ${sales:.2f}")
