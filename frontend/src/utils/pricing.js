/**
 * ShopWave — E-Commerce Pricing & Tax Calculation Utilities
 * 
 * Intentional Compile-Time Syntax Error:
 *  - Bug #6: Typo in keyword 'cosnt' instead of 'const'
 */

// BUG #6 (Intentional Compile-Time Syntax Error):
// Typo in keyword 'cosnt' instead of 'const'.
// V8/Babel/Vite raises: SyntaxError: Unexpected identifier 'SALES_TAX_RATE'
cosnt SALES_TAX_RATE = 0.085;
export const FREE_SHIPPING_THRESHOLD = 99.00;

export function calculateOrderSummary(subtotal) {
    const tax = subtotal * 0.085;
    const shipping = subtotal >= FREE_SHIPPING_THRESHOLD ? 0.00 : 12.50;
    const total = subtotal + tax + shipping;

    return {
        subtotal: Number(subtotal.toFixed(2)),
        tax: Number(tax.toFixed(2)),
        shipping: Number(shipping.toFixed(2)),
        total: Number(total.toFixed(2))
    };
}