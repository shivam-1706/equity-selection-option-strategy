import math
import pandas as pd

class ProtectivePutStrategy:
    """
    Algorithmic execution model for an NSE Protective Put strategy on ITC.NS.
    Combines underlying common equity holding with systematic downside put hedges.
    """
    def __init__(self, capital_base=10000000.0):
        self.ticker = "ITC.NS"
        self.capital_base = capital_base
        self.lot_size = 1600          # Standard NSE derivative lot size rule for ITC
        self.slippage_per_lot = 240.0 # INR 0.15 per share execution cushion friction
        self.transaction_cost = 0.0006 # STT + exchange turnover fees (0.06%)
        
        # Tail-risk insurance floor strike set roughly 5% below baseline intrinsic valuation thresholds
        self.put_strike = 265
        
    def calculate_position_sizing(self, spot_price=281.80):
        """
        Balances common stock weight layers against required option contracts counts.
        """
        put_premium_raw = 3.10
        put_premium_adjusted = put_premium_raw + 0.15 # Accounts for option ask-side slippage markup
        
        # Portfolio Constraint: Allocate roughly 85% of capital to the underlying cash asset base
        target_cash_equity_allocation = self.capital_base * 0.85
        shares_to_buy_raw = target_cash_equity_allocation / spot_price
        
        # Round share count down to align perfectly with derivative lot size boundaries
        target_lots = math.floor(shares_to_buy_raw / self.lot_size)
        total_underlying_shares = target_lots * self.lot_size
        
        underlying_capital_deployed = total_underlying_shares * spot_price
        insurance_premium_outflow = target_lots * (put_premium_adjusted * self.lot_size)
        
        total_capital_outlay = underlying_capital_deployed + insurance_premium_outflow
        cash_buffer_reserve = self.capital_base - total_capital_outlay
        
        execution_metrics = {
            "Strategy": "Protective Put",
            "Underlying_Shares_Bought": total_underlying_shares,
            "Underlying_Capital_Cr": round(underlying_capital_deployed, 2),
            "Put_Insurance_Strike": self.put_strike,
            "Hedge_Put_Contracts_Bought": target_lots,
            "Option_Premium_Outflow": round(insurance_premium_outflow, 2),
            "Friction_Slippage_Loss": round(target_lots * self.slippage_per_lot, 2),
            "Portfolio_Cash_Reserve": round(cash_buffer_reserve, 2),
            "Absolute_Risk_Floor_Price": self.put_strike
        }
        return execution_metrics

if __name__ == "__main__":
    strategy = ProtectivePutStrategy()
    metrics = strategy.calculate_position_sizing()
    df = pd.DataFrame([metrics])
    print("================================================================")
    print("             PROTECTIVE PUT ALGORITHMIC ARCHITECTURE            ")
    print("================================================================")
    for k, v in metrics.items():
        print(f"{k:<30} : {v}")
    print("================================================================")
