<!--
  ShopWave — Product Card Component (Svelte 4 SFC)
  Intentional Compile-Time Template Syntax Error:
    - Bug #7: ParseError: Expected {/if} before EOF
-->
<script>
  export let product;
  export let onAddToCart;
</script>

<div class="product-card glass-panel">
  <div class="product-badge-row">
    <span class="category-tag">{product.category}</span>
    
    <!-- BUG #7 (Intentional Compile-Time Svelte Template Syntax Error):
         Missing closing {/if} block tag!
         Svelte compiler raises: ParseError: Expected {/if} before EOF
    -->
    {#if product.in_stock}
      <span class="stock-badge in">In Stock</span>
    <!-- Missing {/if} closing tag -->
  </div>

  <h3 class="product-title">{product.title}</h3>

  <div class="product-meta">
    <div class="rating-box">
      <span class="star">★</span>
      <span class="rating-val">{product.rating}</span>
    </div>
    <div class="price-val">${Number(product.price).toFixed(2)}</div>
  </div>

  <button 
    class="btn btn-add" 
    disabled={!product.in_stock} 
    on:click={() => onAddToCart && onAddToCart(product)}
  >
    {product.in_stock ? 'Add to Cart 🛒' : 'Out of Stock'}
  </button>
</div>