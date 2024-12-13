# Mock data for the order's cart items
order = {
    "cart_items": [
        {"item_code": "ITEM001", "qty": "2", "item_group": "Empty Bottle"},
        {"item_code": "ITEM002", "qty": "1", "item_group": "gr"},
        {"item_code": "ITEM003", "qty": "5", "item_group": "Groceries"},
        {"item_code": "ITEM004", "qty": "1", "item_group": "Empty Bottle"}
    ]
}

# Required variables
pos_profile = "POS001"  # Example POS profile
posting_date = "2024-12-06"  # Example posting date
doc_name = None  # Initialize doc_name as None

# Mock implementation of the add_to_cart_impl function
def add_to_cart_impl(payload):
    print(f"Adding item to cart with payload: {payload}")
    return {"name": f"doc_{payload['item_code']}"}


for item in order["cart_items"]:
    if doc_name is None and int(item["qty"]) > 0 and item["item_group"] != 'Empty Bottle':
        item_payload = {
            "item_code": item["item_code"],
            "qty": int(item["qty"]),
            "pos_profile": pos_profile,
            "posting_date": posting_date
        }
        res = add_to_cart_impl(item_payload)
        doc_name = res["name"]

if doc_name:
    print(f"First document created: {doc_name}")
else:
    print("No items were added to the cart.")
