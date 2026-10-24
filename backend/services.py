"""
ShopWave — Cart & Checkout Business Logic
Intentional Runtime Errors:
  - Bug #3: NameError: name 'uuid4' is not defined
  - Bug #5: TypeError: 'NoneType' object is not subscriptable
"""

from database import db

def process_checkout(cart_items, customer_email):
    """
    Processes an order, calculates total, and assigns a generated order UUID.
    """
    total = 0.0
    for item in cart_items:
        prod = db.get_by_id(item["product_id"])
        if prod:
            total += prod["price"] * item.get("quantity", 1)

    # BUG #3 (Intentional Runtime NameError):
    # 'uuid4' is invoked here without having been imported from the uuid module!
    # Python raises: NameError: name 'uuid4' is not defined
    try:
        order_token = str(uuid4())
    except NameError as err:
        print(f"[Runtime NameError Bug #3 Detected]: {err}")
        order_token = "order-fallback-token-1234"
        raise err

    return {
        "orderId": order_token,
        "total": round(total, 2),
        "status": "confirmed",
        "customerEmail": customer_email
    }

def get_product_discount_rate(product_id):
    """
    Fetches the discount percentage for a product.
    """
    prod = db.get_by_id(product_id)
    if not prod:
        return 0

    # BUG #5 (Intentional Runtime TypeError):
    # prod["discount"] is None for prod-2, prod-4, and prod-5!
    # Attempting prod["discount"]["percentage"] raises:
    # TypeError: 'NoneType' object is not subscriptable
    try:
        discount_percentage = prod["discount"]["percentage"]
        return discount_percentage
    except TypeError as err:
        print(f"[Runtime TypeError Bug #5 Detected]: {err}")
        raise err