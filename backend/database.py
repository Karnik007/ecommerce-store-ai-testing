"""
ShopWave — In-Memory Inventory Data Store
Intentional Runtime Error:
  - Bug #4: AttributeError: 'list' object has no attribute 'values'
"""

class ProductDatabase:
    def __init__(self):
        self.products = [
            {
                "id": "prod-1",
                "title": "Quantum Pro Wireless Headphones",
                "price": 199.99,
                "category": "Audio",
                "rating": 4.8,
                "in_stock": True,
                "discount": {"code": "SUMMER10", "percentage": 10}
            },
            {
                "id": "prod-2",
                "title": "ErgoMechanical RGB Keyboard",
                "price": 149.50,
                "category": "Peripherals",
                "rating": 4.9,
                "in_stock": True,
                "discount": None  # Triggers Bug #5 if accessed without null check
            },
            {
                "id": "prod-3",
                "title": "Ultra-Wide 4K Curved Monitor (34-inch)",
                "price": 589.00,
                "category": "Displays",
                "rating": 4.7,
                "in_stock": True,
                "discount": {"code": "DISPLAY15", "percentage": 15}
            },
            {
                "id": "prod-4",
                "title": "Precision Wireless Gaming Mouse",
                "price": 79.99,
                "category": "Peripherals",
                "rating": 4.6,
                "in_stock": False,
                "discount": None
            },
            {
                "id": "prod-5",
                "title": "MagSafe Fast Charging Station",
                "price": 49.99,
                "category": "Accessories",
                "rating": 4.5,
                "in_stock": True,
                "discount": None
            }
        ]
        self._next_id = 6

    def get_all(self):
        return list(self.products)

    def get_by_id(self, product_id):
        return next((p for p in self.products if p["id"] == product_id), None)

    def get_all_product_values(self):
        # BUG #4 (Intentional Runtime AttributeError):
        # 'self.products' is a Python list, but code calls '.values()' as if it were a dictionary!
        # Python raises: AttributeError: 'list' object has no attribute 'values'
        try:
            return list(self.products.values())
        except AttributeError as err:
            print(f"[Runtime AttributeError Bug #4 Detected]: {err}")
            raise err

    def add_product(self, data):
        new_prod = {
            "id": f"prod-{self._next_id}",
            "title": data.get("title", "New Product"),
            "price": float(data.get("price", 0.0)),
            "category": data.get("category", "General"),
            "rating": 5.0,
            "in_stock": data.get("in_stock", True),
            "discount": data.get("discount", None)
        }
        self._next_id += 1
        self.products.append(new_prod)
        return new_prod

db = ProductDatabase()