# 🌊 ShopWave — Fullstack Svelte 4 & Python FastAPI AI Benchmark Suite

> **A high-performance e-commerce catalog and inventory management platform built with a Svelte 4 frontend and a Python FastAPI backend, featuring 10 deliberate compile-time and runtime errors for benchmarking AI code-repair systems.**

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/Karnik007/ecommerce-store-ai-testing)
[![Frontend](https://img.shields.io/badge/Frontend-Svelte%204%20%7C%20Vite-ff3e00?logo=svelte)](https://github.com/Karnik007/ecommerce-store-ai-testing)
[![Backend](https://img.shields.io/badge/Backend-Python%203%20%7C%20FastAPI-009688?logo=fastapi)](https://github.com/Karnik007/ecommerce-store-ai-testing)
[![AI Benchmark](https://img.shields.io/badge/AI%20Benchmark-Strict%20Compile%20%26%20Runtime%20Errors-purple)](#error-manifest-summary)

---

## 🎯 Benchmark Objective

ShopWave benchmarks automated AI repair pipelines against **strict language parser and compiler diagnostics**:
- **Compile-Time & Syntax Errors**: Python AST compilation errors, missing colons, unclosed decorator parentheses, Svelte Single File Component template block errors (`ParseError: Expected {/if}`), and CSS property typos.
- **Runtime Exceptions**: `NameError`, `AttributeError`, `TypeError`, and `ReferenceError`.
- **Automated Verification**: Python unittest runner (`backend/test_backend.py`) and browser-based Svelte test assertions (`frontend/frontend_tests.html`).

---

## 📁 Repository Structure

```
ecommerce-store-ai-testing/
├── backend/                                           # Python 3 FastAPI REST API
│   ├── main.py                                        # FastAPI server + native fallback (Contains Error #2)
│   ├── database.py                                    # Inventory store (Contains Runtime AttributeError #4)
│   ├── services.py                                    # Cart & checkout (Contains Errors #3, #5)
│   ├── schemas.py                                     # Pydantic schemas (Contains Compile Error #1)
│   ├── test_backend.py                                # Python unittest evaluation suite
│   └── requirements.txt                               # FastAPI, Uvicorn, Pydantic dependencies
│
├── frontend/                                          # Svelte 4 Application (Vite)
│   ├── package.json                                   # Svelte 4, Vite dependencies
│   ├── vite.config.js                                 # Vite configuration
│   ├── index.html                                     # Entry HTML host
│   ├── frontend_tests.html                            # In-browser test runner
│   ├── frontend_tests.js                              # Svelte evaluation assertions
│   └── src/
│       ├── main.js                                    # Svelte root bootstrap
│       ├── App.svelte                                 # Main storefront dashboard
│       ├── styles.css                                 # Stylesheet (Contains CSS Error #8)
│       ├── components/
│       │   ├── Navbar.svelte                          # Contains Runtime Error #10
│       │   ├── ProductCard.svelte                     # Contains Compile Template Error #7
│       │   └── CartDrawer.svelte                      # Contains Runtime Error #9
│       └── utils/
│           └── pricing.js                             # Contains Compile Error #6
│
├── requirements.txt                                   # Master environment specifications
├── bugs.md                                            # Ground Truth Master Solution Key
└── README.md                                          # Project documentation
```

---

## 🚀 How to Run

### 1. Backend (Python FastAPI)
```bash
cd backend
python -m pip install -r requirements.txt  # Optional: runs in native mode without pip
python main.py
```
The REST API starts at `http://localhost:8000/api/products`.

To run the backend test suite:
```bash
python test_backend.py
```

### 2. Frontend (Svelte 4)
```bash
cd frontend
npm install
npm run dev
```
Or open `frontend/frontend_tests.html` directly in any web browser to run the client-side error assertions.

---

## 🐞 Error Manifest Summary

| ID | Stack | Type | Target File | Description |
|---|---|---|---|---|
| **1** | FastAPI | SyntaxError | `schemas.py` | Missing colon `:` in `class ProductBase(BaseModel)` |
| **2** | FastAPI | SyntaxError | `main.py` | Unclosed parenthesis in `@app.get("/api/products"` |
| **3** | FastAPI | NameError | `services.py` | Undeclared function `uuid4()` without import |
| **4** | FastAPI | AttributeError | `database.py` | Calling `.values()` on a Python list |
| **5** | FastAPI | TypeError | `services.py` | Subscripting `NoneType` on `prod["discount"]["percentage"]` |
| **6** | Svelte | SyntaxError | `utils/pricing.js` | Keyword typo `cosnt SALES_TAX_RATE` |
| **7** | Svelte | Template Error | `components/ProductCard.svelte` | Unterminated `{#if}` block without `{/if}` |
| **8** | Svelte | CSS Syntax | `styles.css` | Property typo `backgroud-color` |
| **9** | Svelte | TypeError | `components/CartDrawer.svelte` | Calling `.reduce()` on `undefined` |
| **10**| Svelte | ReferenceError | `components/Navbar.svelte` | Undeclared function `triggerWishlistModal` |

Detailed solutions, AST traces, and diffs are cataloged in [bugs.md](bugs.md).

---

## 📄 License
MIT License. Created for AI code-repair and automated testing experiments.