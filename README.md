# Quantitative Equity Selection, Valuation Modeling, and Derivatives Strategy Optimization

## Executive Project Dashboard
An institutional-grade quantitative framework designed to screen the **NIFTY 50 universe** for high-quality equities, compute their fundamental intrinsic value via a two-stage **Discounted Cash Flow (DCF)** system, and backtest strategic derivative overlays (**Bull Call Spread** vs. **Protective Put**) under a single uniform volatility regime.

The core objective of this project is to model, implement, and evaluate systematic asset allocation workflows. Instead of reviewing purely which methodology generates the highest top-line absolute profit, this analysis highlights critical execution-layer trade-offs: evaluating **drawdown efficiency, capital preservation, and portfolio stability** across a rolling 24-month high-volatility market cycle using verified corporate parameters for **ITC Limited (`ITC.NS`)**.

---

## Repository Structure
```text
├── data/
│   ├── raw_nifty50_dump.csv                <- Phase 1: Audited universe metrics
│   ├── itc_3_statement_forecast.csv        <- Phase 4: Five-year forecasting engine outputs
│   ├── itc_valuation_matrix_output.csv      <- Phase 5: Valuation metrics output sheet
│   ├── itc_strategy_implementation.csv     <- Phase 7: Position sizing ledger
│   ├── itc_backtest_performance_metrics.csv <- Phase 8 & 9: Backtest dashboard results
│   └── itc_strategic_comparison_matrix.csv <- Phase 10: Comprehensive analytical review
│
├── strategy/
│   ├── investment_view_config.json         <- Phase 6: Core strategic direction mapping
│   ├── verify_view.py                      <- Phase 6: Thesis validation script
│   ├── bull_call_spread.py                 <- Phase 7: Spread implementation model
│   ├── protective_put.py                   <- Phase 7: Protective put implementation model
│   └── strategic_comparison.py             <- Phase 10: Comparison analytics engine
│
└── src/
    ├── financial_model.py                  <- Phase 4: Financial forecast data model
    ├── valuation_model.py                  <- Phase 5: Two-stage DCF equation pipeline
    └── backtest_engine.py                  <- Phase 8 & 9: Backtest risk performance engine
```

---

## Phase 1 & 2: Investment Universe Screening
The quantitative engine filtered large-cap Indian corporations constituting the core equity index using standard corporate structural boundaries to eliminate weak or over-leveraged entities.

### Screening Filters
* **Return on Equity (ROE)**: `> 18.0%` baseline operational efficiency requirement.
* **Top-line Growth**: Revenue CAGR `> 8.0%` over a rolling 5-year historical horizon.
* **Financial Leverage Floor**: Debt to Equity Ratio (`D/E`) `< 0.30` to eliminate structural insolvency risks.
* **Liquidity Security Check**: Robust, consistently positive standalone operational Free Cash Flow.

### Verified Screening Metrics Table

| Company Name | Ticker Symbol | ROE (%) | 5Y Revenue CAGR | Debt/Equity | Free Cash Flow (Cr) | Screener Score |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **ITC Limited** | **ITC.NS** | **28.40%** | **8.60%** | **0.00** | **₹12,180** | **9.4 / 10** |
| TCS Limited | TCS.NS | 51.80% | 11.50% | 0.01 | ₹38,140 | 9.2 / 10 |
| Hindustan Unilever | HINDUNILVR.NS | 29.10% | 9.30% | 0.03 | ₹6,120 | 8.5 / 10 |
| Infosys Limited | INFY.NS | 31.80% | 11.80% | 0.06 | ₹20,100 | 8.1 / 10 |
| Titan Company | TITAN.NS | 30.20% | 16.50% | 0.64 | -₹1,430 | 7.3 / 10 |

**Screener Conclusion & Selection Rationale**: **ITC Limited (`ITC.NS`)** was selected as our core long asset. While technology stocks like TCS offer higher standalone ROE metrics, ITC exhibits pristine balance sheet strength with absolute zero net debt, shielding it against broader global interest rate fluctuations and providing a reliable margin of safety.

---

## Phase 3: Deep Fundamental Analysis
* **Business Model & Revenue Drivers**: A premium diversified consumer goods conglomerate operating across FMCG-Cigarettes, FMCG-Others (Aashirvaad, Sunfeast, Bingo), Paperboards & Specialty Papers, Agri-Business, and separately listed hospitality networks. Pricing power in the formal tobacco segment commands a `>75%` domestic volume dominance, functioning as an inflation-resilient cash engine. This steady operating cash stream finances the scaling of younger digital consumer brands and the asset-right demerger of its luxury hotel business segment.
* **Sustainable Competitive Advantages (Moat)**: Massive, vertically integrated domestic agricultural supply chains coupled with an unparalleled retail distribution network of over 7 million retail touchpoints across India, creating structural efficiencies that competitors cannot replicate.
* **Industry Outlook & Growth Catalysts**: Favorable tailwinds driven by rapid consumption premiumization across middle-class consumption patterns in India. Value hidden within legacy capital allocation silos is being actively unlocked by carving off asset-heavy hotel infrastructures into independent corporate entities.
* **Key Risks Matrix**: Revisions to tobacco excise tax structures, volatile underlying raw agri-commodity cost inputs (such as leaf tobacco price cycles), and execution delays during major structural corporate restructurings.

---

## Phase 4: Financial Modeling (5-Year Forecast Engine)
*All figures are denominated in Indian Rupees (INR Crore), using audited baseline metrics.*

### Modeling Assumptions
* **Revenue Growth Rate**: Normalized at `8.5%` annually, reflecting realistic domestic consumer demand cycles.
* **EBITDA Margin Profile**: Forecasted stable at `35.2%` via cost optimization and high-margin premium tobacco product mix improvements.
* **Effective Corporate Tax Rate**: Pinned at the standard Indian corporate tax tier of `25.17%`.

### 5-Year Forecast Outputs

| Income Statement Item | FY2026 (Base) | FY2027 (E) | FY2028 (E) | FY2029 (E) | FY2030 (E) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Total Revenue** | **₹70,250** | **₹76,221** | **₹82,700** | **₹89,729** | **₹97,356** |
| EBITDA | ₹24,728 | ₹26,830 | ₹29,110 | ₹31,585 | ₹34,269 |
| EBIT (Operating Income) | ₹22,901 | ₹24,848 | ₹26,960 | ₹29,252 | ₹31,738 |
| **PAT (Net Profit)** | **₹17,137** | **₹18,594** | **₹20,174** | **₹21,889** | **₹23,749** |
| **Free Cash Flow (FCF)** | **₹12,180** | **₹13,215** | **₹14,338** | **₹15,557** | **₹16,880** |

---

## Phase 5: Intrinsic & Relative Valuation

### 1. Two-Stage Discounted Cash Flow (DCF) Model
* **Initial Free Cash Flow Base (\(FCF_1\))**: ₹13,215 Crore
* **Cost of Capital (WACC)**: Derived via CAPM at **\(11.25\%\)**, utilizing a risk-free rate of `7.15%` (India 10Y Benchmark G-Sec Yield), a systematic equity beta of `0.78`, and a conservative equity risk premium of `5.25%`. Matches WACC directly since long-term debt is near zero.
* **Sustainable Terminal Growth Rate (\(g_n\))**: Anchored at `5.5%`, matching India's expected long-term structural economic growth.

$$\text{PV of Explicit Cash Flows} = \sum_{t=1}^{5} \frac{FCF_t}{(1 + \text{WACC})^t} = \text{₹53,924 Crore}$$

$$\text{Terminal Value (TV)} = \frac{FCF_5 \times (1 + g_n)}{\text{WACC} - g_n} = \text{₹16,880  1.055}{0.1125 - 0.055} = \text{₹309,711 Crore}$$

$$\text{PV of Terminal Value} = \frac{\text{₹309,711}}{(1 + 0.1125)^5} = \text{₹181,732 Crore}$$

$$\text{Total Firm Intrinsic Value} = \text{₹53,924} + \text{₹181,732} = \text{₹235,656 Crore}$$

Dividing the estimated equity capitalization layer across the actual \(1,252.95\text{ Crore outstanding shares}\) yields a calculated **DCF Intrinsic Value of ₹188.08 per share**.

### 2. Market Relative Valuation Matrix
* **Current Spot Price Reference**: ₹420.00 per share (Reflecting realistic trading ranges)
* **Trailing Price-to-Earnings Ratio (P/E)**: **\(25.6\times\)**
* **FMCG Peer Benchmark Forward Multiple**: Pinned at `38.5x`.

Applying a blended valuation framework (\(70\%\) weighting on our conservative structural DCF and \(30\%\) weighting on peer relative forward multiples), the **Target Fair Value is established at ₹251.60**.

**Valuation Conclusion**: Comparing this target with the live market spot level of **₹420.00**, the asset trades at a premium to its long-term fundamental floor. This sets up a highly realistic market scenario: while the company is a cash-generating powerhouse, entering at current levels requires robust derivative option architectures to protect capital against sudden mean-reversion volatility and broader macroeconomic shifts.

---

## Phase 6 & 7: Options Execution Framework

### Scenario A — Moderate Bullish Regime (Bull Call Spread Structure)
* **Execution Hypothesis**: "The stock is in a steady consolidation channel but faces minor overhead technical resistance near the ₹440 marker. I want to participate in steady growth while keeping risk premium outlays minimal."
* **Strategy Selection**: Buy 1 ATM Call Option / Sell 1 OTM Call Option.
* **Why Not a Naked Long Call?**: Naked options expose capital to steep time-decay (\(Theta\)) risk if the underlying consolidates sideways. The short leg acts as a subsidy, directly funding the long position and insulating the trade against premium decay.
* **Why Not a Covered Call?**: Covered calls limit structural upside flexibility if the asset breaks out sharply, and provide virtually zero true downside capital preservation.

#### Strategy Implementation Mechanics
* **Long Leg (Buy)**: 1 x ATM Strike **₹420 Call Option (CE)** | Premium Cost: ₹12.40 per share.
* **Short Leg (Sell)**: 1 x OTM Strike **₹440 Call Option (CE)** | Premium Credit: ₹3.80 per share.
* **Net Debit Cost Profile**: **₹8.60 per share** (Capping maximum risk at ₹13,760 per standard 1,600 lot contract).

### Scenario B — High-Conviction Long-Term Bullish Regime (Protective Put Structure)
* **Execution Hypothesis**: "I intend to maintain a large underlying stock position due to its high dividend yield, but I require robust downside protection against broader market pullbacks or sector shocks."
* **Strategy Selection**: Hold Equity + Buy 1 OTM Put Option.
* **Why Not a Naked Long Call?**: A long option contract does not capture corporate dividend distributions, resulting in substantial yield sacrifice over a multi-month timeline.

#### Strategy Implementation Mechanics
* **Core Asset Allocation**: Long **ITC Underlying Common Equity** at Spot Market Price: ₹420.00.
* **Hedge Asset (Buy)**: 1 x OTM Strike **₹395 Put Option (PE)** | Premium Cost: ₹4.20 per share.
* **Risk Floor Setting**: The asset downside risk profile is effectively locked at ₹395.00, meaning the maximum absolute loss is capped at a manageable `6.9%` regardless of market pullbacks.

---

## Phase 8 & 9: Backtest & Performance Evaluation
A historical backtest was executed over a 24-month horizon tracking an initial capital allocation base of ₹10,000,000 with monthly option contract rollover schedules under identical volatility conditions.

### Strategy Backtest Performance Dashboard

| Performance Analysis Metric | Buy & Hold Equity | Bull Call Spread | Protective Put |
| :--- | :---: | :---: | :---: |
| **Compound Annual Growth Rate (CAGR)** | 14.85% | 10.20% | **12.40%** |
| **Annualized Portfolio Volatility** | 18.90% | **11.10%** | 12.35% |
| **Maximum Peak-to-Trough Drawdown** | -21.40% | **-6.50%** | -8.20% |
| **Sharpe Ratio (Risk-Adjusted Performance)**| 0.52 | 0.47 | **0.60** |
| **Sortino Ratio (Downside Deviations)** | 0.68 | 0.63 | **0.84** |
| **Calmar Ratio (Drawdown Efficiency)** | 0.69 | **1.56** | 1.51 |
| Total Contract Trade Executions | 1 (Core Buy) | 48 Legs | 24 Legs |
| Winning Trade Percentages | N/A | 58.30% | 37.50% |

---

## Phase 10: Strategic Trade-Off Analysis

Instead of focusing solely on absolute raw returns, the choice of strategy depends on clear risk-adjusted trade-offs:

* **When is a Bull Call Spread preferable?**: This strategy is highly effective during quiet, range-bound market environments. It reduces capital requirements, limits downside risk, and avoids the negative drag of time decay (\(Theta\)) when the stock experiences sideways volatility.
* **When is a Protective Put preferable?**: This strategy is optimal for long-term compounders. It allows the portfolio to benefit from unlimited upside performance and collect steady dividend payouts (`3.5%`–`5.0%` historical yield range), while keeping an absolute floor to limit tail-risk losses during sharp market declines.
* **The structural cost of market insurance**: Implementing a Protective Put reduces the absolute portfolio return by roughly **\(2.45\%\) in CAGR** compared to pure unhedged equity, due to recurring option premium expenses. 
* **Drawdown optimization advantages**: This premium expense is offset by a **\(13.20\%\) improvement in Maximum Drawdown protection**. By limiting downside risk, the strategy achieves a significantly higher **Sortino Ratio (0.84 vs 0.68)**, demonstrating that systematic hedging improves long-term portfolio stability and enhances risk-adjusted returns without relying on directionally unhedged market exposure.

---

## Execution Guide

### Running the Verification Pipeline
The source repository contains automated verification handlers to display dataset models directly via local prompt interfaces.

1. **Verify Strategy View Configurations**:
   ```bash
   python strategy/verify_view.py
   ```
2. **Execute Three-Statement Forecast Sheet**:
   ```bash
   python src/financial_model.py
   ```
3. **Execute Two-Stage DCF In intrinsic Valuation Curves**:
   ```bash
   python src/valuation_model.py
   ```
4. **Display Strategic Performance Trade-Off Summary**:
   ```bash
   python strategy/strategic_comparison.py
   ```

---

## License
This project framework is developed solely for educational and portfolio backtesting evaluation use-cases. Standard derivatives trading involves substantial financial exposure boundaries; simulated historical parameters do not serve as absolute indicators of future execution returns.
