/**
 * ShopWave — Svelte 4 Frontend Automated Benchmark Suite
 * Evaluates whether the AI model has corrected the 5 frontend compile-time and runtime errors.
 */

const SvelteTestSuite = {
    results: [],

    assert(description, passed, details = "") {
        this.results.push({ description, passed: Boolean(passed), details });
    },

    async runAll() {
        this.results = [];

        // ----------------------------------------------------
        // Test 6: Compile-Time SyntaxError 'cosnt' in pricing.js
        // ----------------------------------------------------
        let hasCosntTypo = false;
        try {
            const code = await fetch('src/utils/pricing.js').then(r => r.text());
            hasCosntTypo = /cosnt\s+SALES_TAX_RATE/.test(code);
        } catch (e) {
            hasCosntTypo = true;
        }
        this.assert(
            "Bug #6 (Compile-Time / SyntaxError): pricing.js uses valid 'const' instead of 'cosnt'",
            !hasCosntTypo,
            "SyntaxError: Found 'cosnt SALES_TAX_RATE' in src/utils/pricing.js"
        );

        // ----------------------------------------------------
        // Test 7: Compile-Time Svelte Template Error in ProductCard.svelte
        // ----------------------------------------------------
        let hasUnterminatedIfBlock = false;
        try {
            const code = await fetch('src/components/ProductCard.svelte').then(r => r.text());
            const openIfCount = (code.match(/\{#if/g) || []).length;
            const closeIfCount = (code.match(/\{\/if\}/g) || []).length;
            hasUnterminatedIfBlock = openIfCount !== closeIfCount;
        } catch (e) {
            hasUnterminatedIfBlock = true;
        }
        this.assert(
            "Bug #7 (Compile-Time / Svelte Template): ProductCard.svelte has matching {#if} and {/if} blocks",
            !hasUnterminatedIfBlock,
            "ParseError: Expected {/if} before EOF in ProductCard.svelte"
        );

        // ----------------------------------------------------
        // Test 8: Compile-Time / CSS Property Typo in styles.css
        // ----------------------------------------------------
        let hasCssTypo = false;
        try {
            const code = await fetch('src/styles.css').then(r => r.text());
            hasCssTypo = code.includes("backgroud-color");
        } catch (e) {
            hasCssTypo = true;
        }
        this.assert(
            "Bug #8 (Compile-Time / CSS): styles.css contains no 'backgroud-color' typo",
            !hasCssTypo,
            "CSS property typo: 'backgroud-color' instead of 'background-color' in src/styles.css"
        );

        // ----------------------------------------------------
        // Test 9: Runtime TypeError in CartDrawer.svelte
        // ----------------------------------------------------
        let hasGuardedItemsReduce = false;
        try {
            const code = await fetch('src/components/CartDrawer.svelte').then(r => r.text());
            hasGuardedItemsReduce = /export\s+let\s+items\s*=\s*\[\]/.test(code) || 
                                   /items\?\.reduce/.test(code) || 
                                   /\(items\s*\|\|\s*\[\]\)\.reduce/.test(code);
        } catch (e) {
            hasGuardedItemsReduce = false;
        }
        this.assert(
            "Bug #9 (Runtime TypeError): CartDrawer safely guards against undefined items prop",
            hasGuardedItemsReduce,
            "TypeError: Cannot read properties of undefined (reading 'reduce') in CartDrawer.svelte"
        );

        // ----------------------------------------------------
        // Test 10: Runtime ReferenceError in Navbar.svelte
        // ----------------------------------------------------
        let hasUndeclaredTriggerWishlist = true;
        try {
            const code = await fetch('src/components/Navbar.svelte').then(r => r.text());
            const callsWishlist = code.includes("triggerWishlistModal");
            const declaresWishlist = /function\s+triggerWishlistModal/.test(code) || /const\s+triggerWishlistModal\s*=/.test(code);
            hasUndeclaredTriggerWishlist = callsWishlist && !declaresWishlist;
        } catch (e) {
            hasUndeclaredTriggerWishlist = true;
        }
        this.assert(
            "Bug #10 (Runtime ReferenceError): Navbar declares triggerWishlistModal before invoking in on:click",
            !hasUndeclaredTriggerWishlist,
            "ReferenceError: triggerWishlistModal is not defined in Navbar.svelte"
        );

        return this.results;
    }
};

window.SvelteTestSuite = SvelteTestSuite;