# week7_sales_management.py
# Author: Ongom Ronald

import csv

# -----------------------------
# Data Handling Functions
# -----------------------------
def load_data(filename):
    sales = {}
    try:
        with open(filename, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for item, quantity, price in reader:
                sales[item] = {
                    "quantity": int(quantity),
                    "price": float(price)
                }
    except FileNotFoundError:
        pass
    return sales


def save_data(filename, sales):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for item, data in sales.items():
            writer.writerow([item, data["quantity"], data["price"]])


# -----------------------------
# Sales Functions
# -----------------------------
def add_sale(sales, item, quantity, price):
    if item in sales:
        sales[item]["quantity"] += quantity
        if sales[item]["quantity"] < 0:
            sales[item]["quantity"] = 0
    else:
        sales[item] = {
            "quantity": max(quantity, 0),
            "price": price
        }


def calculate_subtotal(sales):
    return sum(
        data["quantity"] * data["price"]
        for data in sales.values()
    )


def apply_discount(sales, discount_type="none"):
    if not sales or discount_type == "none":
        return 0

    discount = 0
    if discount_type == "bogo":
        for data in sales.values():
            discount += (data["quantity"] // 2) * data["price"]

    return discount


def calculate_tax(amount, tax_rate=0.07):
    return round(amount * tax_rate, 2)


# -----------------------------
# Receipt & Analytics
# -----------------------------
def generate_receipt(sales, subtotal, discount, tax, total):
    print("--- RECEIPT ---")
    for item, data in sales.items():
        print(f"{item}: {data['quantity']} x ${data['price']:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")


def sales_analytics(sales):
    if not sales:
        print("No sales data available.")
        return

    total_items = sum(data["quantity"] for data in sales.values())
    total_sales = calculate_subtotal(sales)
    top_item = max(sales, key=lambda k: sales[k]["quantity"])

    print(f"Top-selling item: {top_item}")
    print(f"Total items sold: {total_items}")
    print(f"Total sales amount: ${total_sales:.2f}")


# -----------------------------
# Main Program Flow
# -----------------------------
def main():
    filename = "sales_data.csv"
    sales = load_data(filename)

    while True:
        print("\nSales Management System")
        print("1. Add Sale")
        print("2. View Receipt")
        print("3. View Sales Analytics")
        print("4. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter unit price: "))
            add_sale(sales, item, quantity, price)

        elif choice == "2":
            subtotal = calculate_subtotal(sales)
            discount = apply_discount(sales, "bogo")
            tax = calculate_tax(subtotal - discount)
            total = subtotal - discount + tax
            generate_receipt(sales, subtotal, discount, tax, total)

        elif choice == "3":
            sales_analytics(sales)

        elif choice == "4":
            save_data(filename, sales)
            break


if __name__ == "__main__":
    main()
