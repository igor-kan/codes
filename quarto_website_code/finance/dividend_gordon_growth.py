"""
Dividend Discount Valuation & Capital Distribution Mechanics.

Implements:
1. Gordon Growth Model P0 = D1 / (r - g)
2. Sustainable Growth Rate (SGR = (1 - Payout) * ROE)
3. Ex-Dividend Price Mechanical Adjustment
"""

def gordon_growth(d0: float, g: float, r: float) -> float:
    if r <= g:
        raise ValueError("Cost of equity r must be strictly greater than perpetual growth rate g!")
    d1 = d0 * (1.0 + g)
    return d1 / (r - g)

def sustainable_growth_rate(payout_ratio: float, roe: float) -> float:
    retention_ratio = 1.0 - payout_ratio
    return retention_ratio * roe

if __name__ == "__main__":
    print("=== GORDON GROWTH DDM ===")
    p0 = gordon_growth(3.50, 0.04, 0.085)
    print(f"Intrinsic share price for D0=$3.50, g=4%, r=8.5%: ${p0:.2f}")
    sgr = sustainable_growth_rate(0.40, 0.18)
    print(f"Sustainable Growth Rate for 40% payout, 18% ROE: {sgr*100:.2f}%")
