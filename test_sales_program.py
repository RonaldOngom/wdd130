import pytest
from week7_sales_management import (
    add_sale,
    calculate_subtotal,
    apply_discount,
    calculate_tax,
    sales_analytics,
    generate_receipt,
    load_data,
    save_data
)

# -----------------------------
# Test Fixtures
# -----------------------------
@pytest.fixture
def sample_sales():
    return {
        "Widget": {"quantity": 3, "price": 10.0},
        "Gadget": {"quantity": 2, "price": 15.0},
        "Thingamajig": {"quantity": 5, "price": 5.0}
    }

@pytest.fixture
def temp_csv(tmp_path):
    """Create a temporary CSV file for load/save tests."""
    file = tmp_path / "sales.csv"
    with open(file, "w") as f:
        f.write("Widget,3,10.0\nGadget,2,15.0\n")
    return file

# -----------------------------
# Test add_sale
# -----------------------------
def test_add_new_sale(sample_sales):
    sales = sample_sales.copy()
    add_sale(sales, "Doohickey", 4, 8.0)
    assert "Doohickey" in sales
    assert sales["Doohickey"]["quantity"] == 4
    assert sales["Doohickey"]["price"] == 8.0

def test_update_existing_sale(sample_sales):
    sales = sample_sales.copy()
    add_sale(sales, "Widget", 2, 10.0)
    assert sales["Widget"]["quantity"] == 5
    assert sales["Widget"]["price"] == 10.0

# -----------------------------
# Test calculate_subtotal
# -----------------------------
def test_calculate_subtotal(sample_sales):
    subtotal = calculate_subtotal(sample_sales)
    expected = (3*10) + (2*15) + (5*5)  # 30+30+25=85
    assert subtotal == expected

# -----------------------------
# Test apply_discount
# -----------------------------
def test_apply_no_discount(sample_sales):
    discount = apply_discount(sample_sales, discount_type="none")
    assert discount == 0

def test_apply_bogo_discount(sample_sales):
    discount = apply_discount(sample_sales, discount_type="bogo")
    # Widget: 3//2=1*10=10, Gadget:2//2=1*15=15, Thingamajig:5//2=2*5=10
    expected = 10 + 15 + 10
    assert discount == expected

# -----------------------------
# Test calculate_tax
# -----------------------------
def test_calculate_tax_default():
    tax = calculate_tax(100)
    assert tax == 7.0

def test_calculate_tax_custom():
    tax = calculate_tax(200, 0.1)
    assert tax == 20.0

# -----------------------------
# Test sales_analytics (outputs)
# -----------------------------
def test_sales_analytics_output(capsys, sample_sales):
    sales_analytics(sample_sales)
    captured = capsys.readouterr()
    assert "Top-selling item" in captured.out
    assert "Total items sold" in captured.out
    assert "Total sales amount" in captured.out

# -----------------------------
# Test generate_receipt (outputs)
# -----------------------------
def test_generate_receipt_output(capsys, sample_sales):
    subtotal = calculate_subtotal(sample_sales)
    discount = apply_discount(sample_sales, "bogo")
    tax = calculate_tax(subtotal - discount)
    total = subtotal - discount + tax
    generate_receipt(sample_sales, subtotal, discount, tax, total)
    captured = capsys.readouterr()
    assert "--- RECEIPT ---" in captured.out
    assert "Subtotal" in captured.out
    assert "Discount" in captured.out
    assert "Tax" in captured.out
    assert "Total" in captured.out

# -----------------------------
# Test load_data and save_data
# -----------------------------
def test_load_data(temp_csv):
    sales = load_data(temp_csv)
    assert sales["Widget"]["quantity"] == 3
    assert sales["Gadget"]["price"] == 15.0

def test_save_data(tmp_path):
    sales = {"ItemA": {"quantity": 2, "price": 5.0}}
    file = tmp_path / "out.csv"
    save_data(file, sales)
    loaded = load_data(file)
    assert loaded == sales

# -----------------------------
# Extra edge-case tests (bonus)
# -----------------------------
def test_add_negative_quantity(sample_sales):
    sales = sample_sales.copy()
    add_sale(sales, "Widget", -1, 10.0)
    assert sales["Widget"]["quantity"] == 2

def test_apply_discount_empty():
    discount = apply_discount({})
    assert discount == 0

def test_generate_receipt_empty(capsys):
    generate_receipt({}, 0, 0, 0, 0)
    captured = capsys.readouterr()
    assert "--- RECEIPT ---" in captured.out
