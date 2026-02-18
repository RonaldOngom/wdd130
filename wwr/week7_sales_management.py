# week7_sales_management.py

TAX_RATE_DEFAULT = 0.07


def add_sale(sales, item_name, quantity, price):
    """
    Add a new sale or update an existing one.
    """
    if item_name in sales:
        sales[item_name]["quantity"] += quantity
        sales[item_name]["price"] = price
    else:
        sales[item_name] = {
            "quantity": quantity,
            "price": price
        }
    return sales


def calculate_subtotal(sales):
    """
    Calculate subtotal of all sales.
    """
    subtotal = 0
    for item in sales.values():
        subtotal += item["quantity"] * item["price"]
    return subtotal


def apply_discount(sales, discount_type="none"):
    """
    Apply discount rules and return discount amount.
    """
    discount = 0

    if discount_type == "bogo":
        for item in sales.values():
            free_items = item["quantity"] // 2
            discount += free_items * item["price"]

    return discount


def calculate_tax(amount, tax_rate=TAX_RATE_DEFAULT):
    """
    Calculate tax for a given amount.
    """
    return round(amount * tax_rate, 2)


def sales_analytics(sales):
    """
    Print sales analytics.
    """
    total_items = sum(item["quantity"] for item in sales.values())
    total_sales = calculate_subtotal(sales)

    top_item = max(sales.items(), key=lambda x: x[1]["quantity"])[0]

    print("Sales Analytics")
    print(f"Top-selling item: {top_item}")
    print(f"Total items sold: {total_items}")
    print(f"Total sales amount: {total_sales:.2f}")


def generate_receipt(sales, subtotal, discount, tax, total):
    """
    Print formatted receipt.
    """
    print("--- RECEIPT ---")
    for name, item in sales.items():
        line_total = item["quantity"] * item["price"]
        print(f"{name}: {item['quantity']} x {item['price']:.2f} = {line_total:.2f}")

    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: -{discount:.2f}")
    print(f"Tax: {tax:.2f}")
    print(f"Total: {total:.2f}")
