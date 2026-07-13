import math
import pandas as pd

class BullCallSpreadStrategy:
    """
    Algorithmic execution model for an NSE Bull Call Spread on ITC.NS.
    Allocates target capital base across structured option legs.
    """
    def __init__(self, capital_base=10000000.0):
        self.ticker = "ITC.NS"
        self.capital_base = capital_base
        self.lot_size = 1600          # Standard NSE derivative lot size rule for ITC
        self.slippage_per_lot = 240.0 # INR 0.15 per share execution cushion friction
        self.transaction_cost = 0.0006 # STT + exchange turnover fees (0.06%)
        
        # Position strikes determined via Phase 5 & 6 parameters
        self.long_strike = 280
        self.short_strike = 300
        
    def calculate_position_sizing(self, spot_price=281.80):
        """
        Computes dynamic contract counts based on structural debit bounds.
        """
        # Baseline premium quotes derived under standard historical implied volatilities (IVs)
        long_premium_raw = 8.50
        short_premium_raw = 2.20
        
        # Adjusting premiums for execution slippage friction layer
        long_premium_adjusted = long_premium_raw + 0.15
        short_premium_adjusted = short_premium_raw - 0.15
        
        net_debit_per_share = long_premium_adjusted - short_premium_adjusted
        net_debit_per_lot = net_debit_per_share * self.lot_size
        
        # Portfolio Constraint: Never risk more than 10% of core capital on pure debit options premiums
        max_premium_risk_allocation = self.capital_base * 0.10
        target_lots = math.floor(max_premium_risk_allocation / net_debit_per_lot)
        
        total_premium_outflow = target_lots * net_debit_per_lot
        total_slippage_cost = target_lots * self.slippage_per_lot
        total_exchange_fees = total_premium_outflow * self.transaction_cost
        
        execution_metrics = {
            "Strategy": "Bull Call Spread",
            "Underlying_Spot": spot_price,
            "Long_Call_Strike": self.long_strike,
            "Short_Call_Strike": self.short_strike,
            "Executed_Lots": target_lots,
            "Total_Contracts": target_lots * 2,
            "Net_Debit_Per_Share": round(net_debit_per_share, 2),
            "Capital_Risk_Outflow": round(total_premium_outflow, 2),
            "Friction_Slippage_Loss": round(total_slippage_cost, 2),
            "Exchange_Turnover_Fees": round(total_exchange_fees, 2)
        }
        return execution_metrics

if __name__ == "__main__":
    strategy = BullCallSpreadStrategy()
    metrics = strategy.calculate_position_sizing()
    df = pd.DataFrame([metrics])
    print("================================================================")
    print("           BULL CALL SPREAD ALGORITHMIC ARCHITECTURE            ")
    print("================================================================")
    for k, v in metrics.items():
        print(f"{k:<25} : {v}")
    print("================================================================")
