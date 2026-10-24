# ShopWave — AI Benchmark Ground Truth Key (Compile-Time & Runtime Errors)

This benchmark evaluates an AI code-repair system across **Python (FastAPI / Pydantic)** and **Svelte 4 (Vite)**.
It contains **strictly Compile-Time SyntaxErrors and Runtime Exceptions** (`TypeError`, `NameError`, `AttributeError`, `ReferenceError`, `ParseError`) with **zero logical errors**.

---

## Master Error Matrix

| ID | Stack | Classification | Target File | Exact Exception / Error |
|---|---|---|---|---|
| **#1** | FastAPI | **Compile-Time** (SyntaxError) | `backend/schemas.py` | `SyntaxError: expected ':'` at line 20 (missing colon in `class ProductBase(BaseModel)`) |
| **#2** | FastAPI | **Compile-Time** (SyntaxError) | `backend/main.py` | `SyntaxError: '(' was never closed` at line 44 (missing closing parenthesis in `@app.get(...)`) |
| **#3** | FastAPI | **Runtime** (NameError) | `backend/services.py` | `NameError: name 'uuid4' is not defined` in `process_checkout()` (missing import) |
| **#4** | FastAPI | **Runtime** (AttributeError) | `backend/database.py` | `AttributeError: 'list' object has no attribute 'values'` in `get_all_product_values()` |
| **#5** | FastAPI | **Runtime** (TypeError) | `backend/services.py` | `TypeError: 'NoneType' object is not subscriptable` on `prod["discount"]["percentage"]` |
| **#6** | Svelte | **Compile-Time** (SyntaxError) | `frontend/src/utils/pricing.js` | `SyntaxError: Unexpected identifier 'SALES_TAX_RATE'` (keyword typo `cosnt`) |
| **#7** | Svelte | **Compile-Time** (Template Error) | `frontend/src/components/ProductCard.svelte` | `ParseError: Expected {/if} before EOF` (unterminated `{#if}` block in template) |
| **#8** | Svelte | **Compile-Time** (CSS Syntax) | `frontend/src/styles.css` | Invalid CSS property: `backgroud-color` instead of `background-color` in `.btn-checkout` |
| **#9** | Svelte | **Runtime** (TypeError) | `frontend/src/components/CartDrawer.svelte` | `TypeError: Cannot read properties of undefined (reading 'reduce')` when prop is omitted |
| **#10**| Svelte | **Runtime** (ReferenceError) | `frontend/src/components/Navbar.svelte` | `ReferenceError: triggerWishlistModal is not defined` (invoked in `on:click` without declaration) |

---

## Detailed Error Specifications & Solutions

### Bug #1: Missing Class Colon (FastAPI Compile-Time SyntaxError)
- **File**: `backend/schemas.py`
- **Error**: `SyntaxError: expected ':'`
- **Buggy Code**:
  ```python
  class ProductBase(BaseModel)
  ```
- **Correction**:
  ```python
  class ProductBase(BaseModel):
  ```
- **Explanation**: Python class definitions require a colon `:` following the class inheritance list.

---

### Bug #2: Unclosed Decorator Parenthesis (FastAPI Compile-Time SyntaxError)
- **File**: `backend/main.py`
- **Error**: `SyntaxError: '(' was never closed`
- **Buggy Code**:
  ```python
  @app.get("/api/products" # BUG #2: Missing closing parenthesis
  def list_products():
  ```
- **Correction**:
  ```python
  @app.get("/api/products")
  def list_products():
  ```
- **Explanation**: Unmatched opening parenthesis causes Python's tokenizer and AST parser to fail during script compilation.

---

### Bug #3: Undeclared `uuid4` Identifier (FastAPI Runtime NameError)
- **File**: `backend/services.py`
- **Error**: `NameError: name 'uuid4' is not defined`
- **Buggy Code**:
  ```python
  order_token = str(uuid4())
  ```
- **Correction**:
  ```python
  from uuid import uuid4
  # ...
  order_token = str(uuid4())
  ```
- **Explanation**: Invoking `uuid4()` without `from uuid import uuid4` raises a `NameError`.

---

### Bug #4: Calling `.values()` on a List (FastAPI Runtime AttributeError)
- **File**: `backend/database.py`
- **Error**: `AttributeError: 'list' object has no attribute 'values'`
- **Buggy Code**:
  ```python
  return list(self.products.values())
  ```
- **Correction**:
  ```python
  return list(self.products)
  ```
- **Explanation**: `self.products` is a Python `list`. Lists do not possess a `.values()` method (which is specific to dictionaries).

---

### Bug #5: Subscripting `NoneType` (FastAPI Runtime TypeError)
- **File**: `backend/services.py`
- **Error**: `TypeError: 'NoneType' object is not subscriptable`
- **Buggy Code**:
  ```python
  discount_percentage = prod["discount"]["percentage"]
  ```
- **Correction**:
  ```python
  discount = prod.get("discount")
  discount_percentage = discount["percentage"] if discount else 0
  ```
- **Explanation**: `prod["discount"]` is `None` for non-discounted products. Accessing `["percentage"]` on `None` throws `TypeError`.

---

### Bug #6: Typo in `const` Keyword (Svelte / JS Compile-Time SyntaxError)
- **File**: `frontend/src/utils/pricing.js`
- **Error**: `SyntaxError: Unexpected identifier 'SALES_TAX_RATE'`
- **Buggy Code**:
  ```javascript
  cosnt SALES_TAX_RATE = 0.085;
  ```
- **Correction**:
  ```javascript
  export const SALES_TAX_RATE = 0.085;
  ```
- **Explanation**: Typo `cosnt` prevents JavaScript engines from compiling the module.

---

### Bug #7: Unterminated Svelte Block (Svelte 4 Template Compile Error)
- **File**: `frontend/src/components/ProductCard.svelte`
- **Error**: `ParseError: Expected {/if} before EOF`
- **Buggy Code**:
  ```svelte
  {#if product.in_stock}
    <span class="stock-badge in">In Stock</span>
  <!-- Missing {/if} closing tag -->
  ```
- **Correction**:
  ```svelte
  {#if product.in_stock}
    <span class="stock-badge in">In Stock</span>
  {/if}
  ```
- **Explanation**: In Svelte templates, all control blocks (`{#if}`, `{#each}`, `{#await}`) must terminate with their matching closing block (`{/if}`, `{/each}`, `{/await}`).

---

### Bug #8: Misspelled CSS Property (Svelte Compile-Time / CSS Syntax Error)
- **File**: `frontend/src/styles.css`
- **Error**: Invalid property declaration
- **Buggy Code**:
  ```css
  .btn-checkout {
      backgroud-color: rgba(6, 182, 212, 0.9);
  }
  ```
- **Correction**:
  ```css
  .btn-checkout {
      background-color: rgba(6, 182, 212, 0.9);
  }
  ```
- **Explanation**: Missing 'n' in `backgroud-color` causes CSS parsers to discard the rule.

---

### Bug #9: Calling `.reduce()` on Undefined (Svelte Runtime TypeError)
- **File**: `frontend/src/components/CartDrawer.svelte`
- **Error**: `TypeError: Cannot read properties of undefined (reading 'reduce')`
- **Buggy Code**:
  ```javascript
  $: subtotal = items.reduce((sum, item) => sum + (item.price * (item.quantity || 1)), 0);
  ```
- **Correction**:
  ```javascript
  export let items = []; // default fallback
  $: subtotal = (items || []).reduce((sum, item) => sum + (item.price * (item.quantity || 1)), 0);
  ```
- **Explanation**: If `items` prop is not passed, calling `.reduce()` directly on `undefined` causes an unhandled `TypeError`.

---

### Bug #10: Undeclared Event Handler (Svelte Runtime ReferenceError)
- **File**: `frontend/src/components/Navbar.svelte`
- **Error**: `ReferenceError: triggerWishlistModal is not defined`
- **Buggy Code**:
  ```svelte
  <button class="btn btn-secondary" on:click={triggerWishlistModal}>
  ```
- **Correction**:
  ```svelte
  <script>
    function triggerWishlistModal() {
      console.log("Wishlist opened");
    }
  </script>
  ```
- **Explanation**: Template event handler `on:click` binds to an identifier that was never declared in `<script>`.