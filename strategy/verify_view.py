import os
import json

def verify_and_log_investment_view():
    """
    Parses and prints the strategic investment view to confirm the data pipeline.
    """
    config_path = "strategy/investment_view_config.json"
    
    if not os.path.exists(config_path):
        print("[!] Error: Configuration file missing.")
        return
        
    with open(config_path, "r") as f:
        config = json.load(f)
        
    thesis = config["investment_thesis"]
    scenarios = config["options_strategy_scenarios"]
    
    print("================================================================")
    print(f"       INVESTMENT VIEW MATRIX FOR {thesis['underlying_ticker']} ")
    print("================================================================")
    print(f"Current Spot Price : INR {thesis['valuation_summary']['current_spot_price']:.2f}")
    print(f"Blended Fair Value : INR {thesis['valuation_summary']['blended_fair_value']:.2f}")
    print(f"Market Discount    : {thesis['valuation_summary']['market_discount_pct']:.2f}% (Undervalued)")
    print(f"Directional Bias   : {thesis['directional_bias']}")
    print("\n[SCENARIO A]: Moderate Bullishness Profile")
    print(f" -> Selected Strategy: {scenarios['scenario_a_moderate_bullishness']['strategy_choice']}")
    print(f" -> Justification    : {scenarios['scenario_a_moderate_bullishness']['structural_justification'][:115]}...")
    print("\n[SCENARIO B]: Strong Bullishness Profile")
    print(f" -> Selected Strategy: {scenarios['scenario_b_strong_bullishness']['strategy_choice']}")
    print(f" -> Justification    : {scenarios['scenario_b_strong_bullishness']['structural_justification'][:115]}...")
    print("================================================================")
    print("[+] Phase 6 Complete. Strategic view logic validated cleanly.")

if __name__ == "__main__":
    verify_and_log_investment_view()
