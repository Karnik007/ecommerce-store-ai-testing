"""
ShopWave â€” FastAPI E-Commerce Application Server
Intentional Compile-Time Syntax Error:
  - Bug #2: SyntaxError: invalid syntax (unclosed parenthesis in decorator or def)
"""

import json
from database import db
from services import process_checkout, get_product_discount_rate

# Attempt schemas import to catch Compile-Time SyntaxError Bug #1
schema_error = None
try:
    import schemas
except SyntaxError as e:
    schema_error = f"{e.__class__.__name__}: {e.msg} at line {e.lineno}"
    print(f"âš ï¸ [Compile-Time SyntaxError in schemas.py]: {schema_error}")

try:
    from fastapi import FastAPI, HTTPException
    from fastapi.middleware.cors import CORSMiddleware
    has_fastapi = True
except ImportError:
    has_fastapi = False

PORT = 8000

if has_fastapi:
    app = FastAPI(title="ShopWave API", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # BUG #2 (Intentional Compile-Time SyntaxError):
    # Missing closing parenthesis ')' in the route decorator header!
    # Python parser raises: SyntaxError: invalid syntax (or closing parenthesis does not match)
    # Uncommenting triggers parse failure:
    # @app.get("/api/products"
    @app.get("/api/products" # BUG #2: Missing closing parenthesis
    def list_products():
        return {"success": True, "data": db.get_all()}

    @app.get("/api/products/{product_id}")
    def get_product(product_id: str):
        prod = db.get_by_id(product_id)
        if not prod:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"success": True, "data": prod}

    @app.get("/api/products/{product_id}/discount")
    def get_discount(product_id: str):
        try:
            rate = get_product_discount_rate(product_id)
            return {"success": True, "discountRate": rate}
        except TypeError as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.get("/api/products/inspect/values")
    def inspect_values():
        try:
            return {"success": True, "data": db.get_all_product_values()}
        except AttributeError as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.post("/api/checkout")
    def checkout(payload: dict):
        try:
            result = process_checkout(payload.get("items", []), payload.get("email", "guest@example.com"))
            return {"success": True, "order": result}
        except NameError as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.get("/api/health")
    def health():
        return {"status": "healthy", "schemaError": schema_error}

    if __name__ == "__main__":
        import uvicorn
        print(f"ðŸš€ ShopWave FastAPI running on http://localhost:{PORT}")
        uvicorn.run(app, host="0.0.0.0", port=PORT)

else:
    # Zero-dependency standard library HTTP Server fallback
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import urlparse

    class NativeRequestHandler(BaseHTTPRequestHandler):
        def _set_headers(self, status=200):
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.end_headers()

        def do_OPTIONS(self):
            self._set_headers(200)

        def do_GET(self):
            parsed = urlparse(self.path)
            if parsed.path == "/api/products":
                self._set_headers(200)
                self.wfile.write(json.dumps({"success": True, "data": db.get_all()}).encode())
            elif parsed.path == "/api/health":
                self._set_headers(200)
                self.wfile.write(json.dumps({"status": "healthy", "schemaError": schema_error}).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Not Found"}).encode())

    if __name__ == "__main__":
        server = HTTPServer(("0.0.0.0", PORT), NativeRequestHandler)
        print(f"ðŸš€ ShopWave (Native Python Server) running on http://localhost:{PORT}")
        server.serve_forever()