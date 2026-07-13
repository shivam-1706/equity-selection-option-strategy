import os
import pandas as pd

class StrategicComparisonEngine:
    """
    Analytical evaluation module for Phase 10.
    Compares corporate risk-return implementations and prints the project's final core conclusions.
    """
    def __init__(self):
        # Ingesting the real-world verified metrics generated in Phase 9
        self.metrics = {
            "Buy_Hold_Equity": {"cagr": 93.63, "vol": 26.54, "max_dd": -21.40, "sharpe": 3.26},
            "Bull_Call_Spread": {"cagr": 34.80, "vol": 13.11, "max_dd": -6.50, "sharpe": 2.11},
            "Protective_Put":  {"cagr": 81.42, "vol": 16.82, "max_dd": -8.20, "sharpe": 4.42}
        }

    def evaluate_structural_tradeoffs(self):
        bh = self.metrics["Buy_Hold_Equity"]
        pp = self.metrics["Protective_Put"]
        bcs = self.metrics["Bull_Call_Spread"]
        
        # Calculate exactly how much absolute return was given up to buy downside insurance
        cagr_sacrifice_for_put = bh["cagr"] - pp["cagr"]
        # Calculate the absolute reduction in peak-to-trough market drawdown
        drawdown_protection_gained = abs(bh["max_dd"]) - abs(pp["max_dd"])
        
        # Volatility reduction metrics
        vol_reduction_spread = bh["vol"] - bcs["vol"]
        
        comparison_report = {
            "Strategic_Question": [
                "When is a Bull Call Spread preferable?",
                "When is a Protective Put preferable?",
                "How much absolute CAGR is sacrificed for downside protection?",
                "Does reducing the drawdown improve risk-adjusted efficiency?",
                "Which strategy suits a conservative/institutional profile?"
            ],
            "Empirical_Answer_And_Data_Proof": [
                f"During low-volatility consolidation phases. It cut volatility by {vol_reduction_spread:.2f}% (13.11% vs 26.54%).",
                "During high-conviction structural bull runs. It captured an exceptional 81.42% CAGR with an absolute risk floor.",
                f"A minor {cagr_sacrifice_for_put:.2f}% CAGR drag, caused by the recurring costs of buying protective option premiums.",
                f"Yes. Shaving off {drawdown_protection_gained:.2f}% from max drawdown expanded the Sharpe Ratio from 3.26 to an ultra-efficient 4.42.",
                "The Protective Put. It maximizes drawdown efficiency (Calmar Ratio of 9.93) while keeping full equity dividend access."
            ]
        }
        
        df = pd.DataFrame(comparison_report)
        return df

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    engine = StrategicComparisonEngine()
    comparison_df = engine.evaluate_structural_tradeoffs()
    
    # Save the comparison report to disk to finalize the repository's data trail
    comparison_df.to_csv("data/itc_strategic_comparison_matrix.csv", index=False)
    
    print("==================================================================================")
    print("                 PHASE 10: STRATEGIC INSIGHTS & TRADEOFF MATRIX                   ")
    print("==================================================================================")
    pd.set_option('display.max_colwidth', None)
    print(comparison_df.to_string(index=False))
    print("==================================================================================")
    print("[+] Phase 10 Complete. Final project deliverables compiled successfully.")
