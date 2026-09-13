"""
Corporate Valuation: Financial Statements Waterfall and Two-Stage DCF.

Implements:
1. P&L to Unlevered Free Cash Flow (FCFF) waterfall
2. DuPont 3-Step Return on Equity (ROE) decomposition
3. Weighted Average Cost of Capital (WACC) with corporate interest tax shield
4. Two-Stage Discounted Cash Flow (DCF) with Gordon growth terminal value
"""

from typing import Dict, List, Tuple

def financial_waterfall(rev: float, cogs: float, sga: float, rd: float, depr: float,
                        amort: float, interest: float, tax_rate: float, capex: float,
                        delta_nwc: float) -> Dict[str, float]:
    gross_profit = rev - cogs
    ebit = gross_profit - sga - rd
    ebitda = ebit + depr + amort
    ebt = ebit - interest
    taxes = max(0.0, ebt * tax_rate)
    net_income = ebt - taxes
    nopat = ebit * (1.0 - tax_rate)
    cfo = net_income + (depr + amort) - delta_nwc
    fcff = nopat + (depr + amort) - capex - delta_nwc
    
    return {
        "revenue": rev, "gross_profit": gross_profit, "ebit": ebit,
        "ebitda": ebitda, "net_income": net_income, "cfo": cfo, "fcff": fcff
    }

def dupont_3step(net_income: float, revenue: float, assets: float, equity: float) -> Tuple[float, float, float, float]:
    margin = net_income / revenue
    turnover = revenue / assets
    leverage = assets / equity
    roe = margin * turnover * leverage
    return margin, turnover, leverage, roe

def calculate_wacc(mkt_cap: float, total_debt: float, rf: float, beta: float,
                   erp: float, cost_debt: float, tax_rate: float) -> float:
    cost_equity = rf + beta * erp
    after_tax_debt = cost_debt * (1.0 - tax_rate)
    v = mkt_cap + total_debt
    return (mkt_cap / v) * cost_equity + (total_debt / v) * after_tax_debt

def dcf_valuation(base_fcff: float, growth_rates: List[float], g_terminal: float,
                  wacc: float, net_debt: float, shares: float) -> float:
    pv_discrete = 0.0
    curr_fcff = base_fcff
    for t, g in enumerate(growth_rates, 1):
        curr_fcff *= (1.0 + g)
        pv_discrete += curr_fcff / ((1.0 + wacc) ** t)
        
    tv = (curr_fcff * (1.0 + g_terminal)) / (wacc - g_terminal)
    pv_tv = tv / ((1.0 + wacc) ** len(growth_rates))
    ev = pv_discrete + pv_tv
    equity_val = ev - net_debt
    return equity_val / shares

if __name__ == "__main__":
    print("=== CORPORATE DCF VALUATION ===")
    wf = financial_waterfall(10000, 4000, 2500, 1000, 600, 150, 200, 0.21, 700, 150)
    print(f"Revenue: ${wf['revenue']}M | EBITDA: ${wf['ebitda']}M | FCFF: ${wf['fcff']}M")
    wacc = calculate_wacc(7500, 3000, 0.042, 1.15, 0.055, 0.055, 0.21)
    print(f"Calculated WACC: {wacc*100:.2f}%")
    p_int = dcf_valuation(wf["fcff"], [0.08, 0.07, 0.06, 0.05, 0.04], 0.025, wacc, 2000, 100)
    print(f"Intrinsic Share Price: ${p_int:.2f}")
