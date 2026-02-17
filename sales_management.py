# week7_sales_management.py
# Author: Ongom Ronald
import csv

# -----------------------------
# Data Handling Functions
# -----------------------------
def load_data(filename):
    """Load sales data from a CSV file."""
    sales = {}
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                item = row[0]
                quantity = int(row[1])
                price = float(row[2])
                sales[item] = {'quantity': quantity, 'price': price}
    except FileNotFoundError:
        print(f"{filename} not found. Starting with empty sales data.")
    return sales

def save_data(filename, sales):
    """Save sales data to a CSV file."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item, data in sales.items():
            writer.writerow([item, data['quantity'], data['price']])

# -----------------------------
# Sales Functions
# -----------------------------
def add_sale(sales, item, quantity, price):
    """Add or update a sale record."""
    if item in sales:
        sales[item]['quantity'] += quantity
        sales[item]['price'] = price  # Update price if changed
    else:
        sales[item] = {'quantity': quantity, 'price': price}
    return sales

def calculate_subtotal(sales):
    """Calculate subtotal of all sales before discount and tax."""
    subtotal = 0
    for data in sales.values():
        subtotal += data['quantity'] * data['price']
    return subtotal

def apply_discount(sales, discount_type="none"):
    """
    Apply discount to sales.
    - "bogo": Buy One Get One Free (applied per item)
    - "none": No discount
    Returns total discount amount.
    """
    discount = 0
    if discount_type.lower() == "bogo":
        for data in sales.values():
            free_items = data['quantity'] // 2
            discount += free_items * data['price']
    return discount

def calculate_tax(amount, tax_rate=0.07):
    """Calculate tax based on given rate (default 7%)."""
    return amount * tax_rate

# -----------------------------
# Receipt & Analytics
# -----------------------------
def generate_receipt(sales, subtotal, discount, tax, total):
    """Print a formatted receipt."""
    print("\n--- RECEIPT ---")
    print("{:<15} {:>8} {:>10} {:>10}".format("Item", "Qty", "Price", "Total"))
    for item, data in sales.items():
        total_price = data['quantity'] * data['price']
        print("{:<15} {:>8} {:>10.2f} {:>10.2f}".format(item, data['quantity'], data['price'], total_price))
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: +${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("---------------\n")

def sales_analytics(sales):
    """Display sales analytics: total sales, top-selling item, total quantity sold."""
    total_sales = calculate_subtotal(sales)
    total_items = sum(data['quantity'] for data in sales.values())
    if sales:
        top_item = max(sales.items(), key=lambda x: x[1]['quantity'])
        print(f"Top-selling item: {top_item[0]} (Qty: {top_item[1]['quantity']})")
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

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter unit price: "))
            sales = add_sale(sales, item, quantity, price)
            print(f"Added/Updated sale: {item} x{quantity} @ ${price:.2f}")

        elif choice == '2':
            subtotal = calculate_subtotal(sales)
            discount_type = input("Enter discount type (none/bogo): ")
            discount = apply_discount(sales, discount_type)
            tax = calculate_tax(subtotal - discount)
            total = subtotal - discount + tax
            generate_receipt(sales, subtotal, discount, tax, total)

        elif choice == '3':
            sales_analytics(sales)

        elif choice == '4':
            save_data(filename, sales)
            print("Sales data saved. Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
