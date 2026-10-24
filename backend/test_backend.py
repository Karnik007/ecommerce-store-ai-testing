"""
ShopWave — Backend AI Evaluation Test Suite
Evaluates whether the AI bug-fixing model has corrected all 5 backend compile & runtime errors.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class TestFastAPICompileAndRuntimeErrors(unittest.TestCase):

    def test_bug_1_schemas_syntax_compile(self):
        """
        Bug #1 (Compile-Time SyntaxError):
        Verifies that schemas.py compiles without 'SyntaxError: expected :' on class ProductBase
        """
        schemas_path = os.path.join(os.path.dirname(__file__), "schemas.py")
        with open(schemas_path, "r", encoding="utf-8") as f:
            code = f.read()

        try:
            compile(code, schemas_path, "exec")
        except SyntaxError as e:
            self.fail(f"SyntaxError in schemas.py (Bug #1): {e.msg} at line {e.lineno}")

    def test_bug_2_main_decorator_syntax(self):
        """
        Bug #2 (Compile-Time SyntaxError):
        Verifies that main.py has no unclosed parenthesis or syntax errors in route definitions.
        """
        main_path = os.path.join(os.path.dirname(__file__), "main.py")
        with open(main_path, "r", encoding="utf-8") as f:
            code = f.read()

        try:
            compile(code, main_path, "exec")
        except SyntaxError as e:
            self.fail(f"SyntaxError in main.py (Bug #2): {e.msg} at line {e.lineno}")

    def test_bug_3_runtime_name_error_uuid4(self):
        """
        Bug #3 (Runtime NameError):
        Verifies that process_checkout has imported uuid4 and does not raise NameError.
        """
        from services import process_checkout
        try:
            process_checkout([{"product_id": "prod-1", "quantity": 1}], "test@example.com")
        except NameError as e:
            self.fail(f"NameError in process_checkout (Bug #3): {e}")

    def test_bug_4_runtime_attribute_error_list_values(self):
        """
        Bug #4 (Runtime AttributeError):
        Verifies that get_all_product_values does not call .values() on a list.
        """
        from database import db
        try:
            db.get_all_product_values()
        except AttributeError as e:
            self.fail(f"AttributeError in get_all_product_values (Bug #4): {e}")

    def test_bug_5_runtime_type_error_subscript_none(self):
        """
        Bug #5 (Runtime TypeError):
        Verifies that get_product_discount_rate safely handles products with discount=None.
        """
        from services import get_product_discount_rate
        # prod-2 has discount=None
        try:
            rate = get_product_discount_rate("prod-2")
            self.assertIsInstance(rate, (int, float))
        except TypeError as e:
            self.fail(f"TypeError in get_product_discount_rate (Bug #5): {e}")

if __name__ == "__main__":
    print("\n🧪 Running ShopWave Backend AI Benchmark Tests...\n")
    unittest.main(verbosity=2)