<!--
  ShopWave — Shopping Cart Slide-Over Drawer
  Intentional Runtime TypeError:
    - Bug #9: items.reduce called on undefined when prop is omitted
-->
<script>
  export let isOpen = false;
  export let items; // Intentionally omitted default [] to expose Bug #9
  export let onRemove;
  export let onClose;
  export let onCheckout;

  // BUG #9 (Intentional Runtime TypeError):
  // 'items' is not defaulted or guarded against undefined.
  // If <CartDrawer /> is mounted without items or items={undefined},
  // V8 throws: TypeError: Cannot read properties of undefined (reading 'reduce')
  $: subtotal = items.reduce((sum, item) => sum + (item.price * (item.quantity || 1)), 0);
</script>

{#if isOpen}
  <div class="drawer-backdrop" on:click={onClose}>
    <div class="drawer-panel glass-panel" on:click|stopPropagation>
      <div class="drawer-header">
        <h3>Shopping Bag ({items ? items.length : 0})</h3>
        <button class="btn-close" on:click={onClose}>&times;</button>
      </div>

      <div class="drawer-body">
        {#if !items || items.length === 0}
          <div class="empty-cart">
            <span class="empty-icon">🛍️</span>
            <p>Your bag is currently empty.</p>
          </div>
        {:else}
          {#each items as item}
            <div class="cart-item">
              <div>
                <div class="item-title">{item.title}</div>
                <div class="item-qty">Qty: {item.quantity || 1} &bull; ${item.price}</div>
              </div>
              <button class="btn-del" on:click={() => onRemove && onRemove(item.id)}>&times;</button>
            </div>
          {/each}
        {/if}
      </div>

      <div class="drawer-footer">
        <div class="total-row">
          <span>Subtotal</span>
          <span class="subtotal-val">${subtotal.toFixed(2)}</span>
        </div>
        <button class="btn btn-checkout" on:click={onCheckout} disabled={!items || items.length === 0}>
          Proceed to Checkout &rarr;
        </button>
      </div>
    </div>
  </div>
{/if}