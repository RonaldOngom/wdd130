# -----------------------------
# Test add_sale with negative quantity
# -----------------------------
def test_add_sale_negative_quantity(sample_sales):
    sales = sample_sales.copy()
    add_sale(sales, "Widget", -1, 10.0)
    # Quantity should decrease
    assert sales["Widget"]["quantity"] == 2  # 3 - 1

# -----------------------------
# Test apply_discount for empty sales
# -----------------------------
def test_apply_discount_empty():
    discount = apply_discount({})
    assert discount == 0

# -----------------------------
# Test generate_receipt with empty sales
# -----------------------------
def test_generate_receipt_empty(capsys):
    generate_receipt({}, 0, 0, 0, 0)
    captured = capsys.readouterr()
    assert "--- RECEIPT ---" in captured.out
