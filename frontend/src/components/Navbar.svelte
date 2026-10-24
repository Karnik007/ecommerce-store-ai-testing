<!--
  ShopWave — Top Navigation Header
  Intentional Runtime ReferenceError:
    - Bug #10: 'triggerWishlistModal' is called on button click without declaration
-->
<script>
  export let cartCount = 0;
  export let onOpenCart;
  // triggerWishlistModal is intentionally omitted from script to trigger Bug #10!
</script>

<header class="app-header glass-panel">
  <div class="brand">
    <span class="brand-logo">🌊</span>
    <div>
      <h1 class="brand-title">Shop<span>Wave</span></h1>
      <p class="brand-sub">Svelte 4 &amp; Python FastAPI Benchmark</p>
    </div>
  </div>

  <div class="header-right">
    <!-- BUG #10 (Intentional Runtime ReferenceError):
         Clicking this button invokes 'triggerWishlistModal', which is never declared in <script>!
         V8 / Svelte runtime raises: ReferenceError: triggerWishlistModal is not defined
    -->
    <button class="btn btn-secondary" on:click={triggerWishlistModal}>
      ♡ Saved Wishlist
    </button>

    <button class="btn btn-cart" on:click={onOpenCart}>
      Bag 🛒 <span class="cart-badge">{cartCount}</span>
    </button>
  </div>
</header>