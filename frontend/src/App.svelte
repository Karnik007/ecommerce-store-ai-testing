<script>
  import { onMount } from 'svelte';
  import Navbar from './components/Navbar.svelte';
  import ProductCard from './components/ProductCard.svelte';
  import CartDrawer from './components/CartDrawer.svelte';

  let products = [
    { id: "prod-1", title: "Quantum Pro Wireless Headphones", price: 199.99, category: "Audio", rating: 4.8, in_stock: true },
    { id: "prod-2", title: "ErgoMechanical RGB Keyboard", price: 149.50, category: "Peripherals", rating: 4.9, in_stock: true },
    { id: "prod-3", title: "Ultra-Wide 4K Curved Monitor (34-inch)", price: 589.00, category: "Displays", rating: 4.7, in_stock: true },
    { id: "prod-4", title: "Precision Wireless Gaming Mouse", price: 79.99, category: "Peripherals", rating: 4.6, in_stock: false },
    { id: "prod-5", title: "MagSafe Fast Charging Station", price: 49.99, category: "Accessories", rating: 4.5, in_stock: true }
  ];

  let cart = [];
  let isCartOpen = false;
  let activeCategory = 'All';

  onMount(async () => {
    try {
      const res = await fetch('http://localhost:8000/api/products');
      const data = await res.json();
      if (data.success && Array.isArray(data.data)) {
        products = data.data;
      }
    } catch (e) {
      console.log('Backend offline, using fallback catalog');
    }
  });

  $: filteredProducts = activeCategory === 'All' 
    ? products 
    : products.filter(p => p.category === activeCategory);

  $: cartCount = cart.reduce((total, item) => total + (item.quantity || 1), 0);

  function handleAddToCart(product) {
    const existing = cart.find(i => i.id === product.id);
    if (existing) {
      existing.quantity = (existing.quantity || 1) + 1;
      cart = [...cart];
    } else {
      cart = [...cart, { ...product, quantity: 1 }];
    }
    isCartOpen = true;
  }

  function handleRemoveFromCart(id) {
    cart = cart.filter(i => i.id !== id);
  }

  function handleCheckout() {
    alert(`Order placed successfully for ${cartCount} item(s)!`);
    cart = [];
    isCartOpen = false;
  }
</script>

<div class="app-layout">
  <Navbar 
    cartCount={cartCount} 
    onOpenCart={() => isCartOpen = true} 
  />

  <section class="hero-banner glass-panel">
    <div>
      <span class="hero-badge">⚡ Special Summer Catalog</span>
      <h2 class="hero-heading">Elevate Your Digital Workspace</h2>
      <p class="hero-desc">Curated flagship tech hardware and ergonomic peripherals with instant dispatch.</p>
    </div>
  </section>

  <div class="filter-pills">
    {#each ['All', 'Audio', 'Peripherals', 'Displays', 'Accessories'] as cat}
      <button 
        class="filter-chip {activeCategory === cat ? 'active' : ''}" 
        on:click={() => activeCategory = cat}
      >
        {cat}
      </button>
    {/each}
  </div>

  <main class="products-grid">
    {#each filteredProducts as product (product.id)}
      <ProductCard 
        product={product} 
        onAddToCart={handleAddToCart} 
      />
    {/each}
  </main>

  <CartDrawer 
    isOpen={isCartOpen} 
    items={cart} 
    onClose={() => isCartOpen = false} 
    onRemove={handleRemoveFromCart} 
    onCheckout={handleCheckout} 
  />

  <footer class="app-footer">
    <p>ShopWave Svelte 4 &amp; Python FastAPI AI Benchmark &copy; 2026. Built for AI Automated Code Correction &amp; Debugging Evaluations.</p>
  </footer>
</div>