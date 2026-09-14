# Strategic Business Recommendations & Retention Playbook

**Lead Author:** D G N S Widumini (IT24101176) — Business Strategy & Documentation Lead  
**Stakeholder Audience:** Chief Marketing Officer (CMO), Head of Customer Retention, CRM Operations  
**Group ID:** 2026-AI-07  
**Module:** IT3091 Machine Learning Project  

---

### 1. Risk-Tiered Customer Intervention Framework

The champion model (Logistic Regression with balanced weights, calibrated cutoff $\tau^* = 0.44$) outputs individual churn probability scores $P(\text{Churn} = 1 \mid \mathbf{x})$. Customers are categorized into three actionable operational tiers:

| Risk Tier | Churn Probability ($P$) | Cohort Characteristics | Operational Action | Cost per Intervention | Expected Retention Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1: Critical Risk** | $P \ge 0.65$ | Month-to-month contract, Fiber optic, tenure $< 12$ months, Electronic check billing. | **Proactive Concierge Call:** Direct outreach from retention specialist offering a 1-year contract lock-in with a 15% discount or 3 months free streaming add-on. | $50.00 (Agent time + rebate) | 35% churn reduction |
| **Tier 2: Moderate Risk** | $0.40 \le P < 0.65$ | Tech-support unattached, multiple lines, paperless billing without auto-pay. | **Automated Digital CRM Campaign:** Push notification offering free 6-month `TechSupport` / `OnlineSecurity` trial and a $10 credit to set up automated card/bank billing. | $10.00 (Software license + credit) | 22% churn reduction |
| **Tier 3: Low Risk (Safe)** | $P < 0.40$ | Two-year contract, high tenure ($> 24$ months), automatic billing, bundled services. | **Passive Loyalty Maintenance:** Quarterly appreciation emails, priority routing in customer care. No cash discounts (prevents margin dilution). | $0.00 | Organic retention ($< 5\%$ churn) |

---

### 2. Targeted Root-Cause Interventions

Our model's log-odds coefficients and EDA findings isolate three structural churn drivers:

1. **The "Fiber Optic Service Deficit" (Log-Odds: $+0.73$, Churn Rate: $41.89\%$):**
   * *Problem:* Fiber optic customers churn at more than double the rate of DSL users, primarily due to billing friction at high price points ($70–$105/mo) combined with service outages.
   * *Action:* Automatically bundle free `TechSupport` and dedicated line diagnostic checkups for all new fiber activations during the first 90 days.

2. **The "Electronic Check Friction Point" (Log-Odds: $+0.32$, Churn Rate: $45.29\%$):**
   * *Problem:* Manual electronic check payments require active monthly effort and introduce repeated billing friction.
   * *Action:* Introduce an instant recurring bill credit of **$5/month** for transitioning to `Credit card (automatic)` or `Bank transfer (automatic)`. This addresses a driver associated with an immediate 30-percentage-point drop in churn risk.

3. **The "0–12 Month Tenure Cliff" (Churn Rate: $47.68\%$):**
   * *Problem:* Nearly half of all churn occurs during the first year of subscription.
   * *Action:* Introduce an automated "Onboarding Milestone Program" with proactive check-in surveys on Day 14, Day 45, and Day 90 to identify early service dissatisfaction before cancellation occurs.

---

### 3. Financial Cost-Benefit & ROI Analysis

On the 1,409 holdout test customers (with 374 actual churners):
* **Baseline Status Quo (Do Nothing):** 374 churners $\times$ \$500 average customer acquisition cost (CAC) replacement = **\$187,000 lost revenue**.
* **Standard Threshold ($\tau = 0.50$):** Total financial liability = **\$53,950** (FN: 82 missed churners $\times$ \$500 + FP: 259 false alarms $\times$ \$50).
* **Optimized Cutoff ($\tau^* = 0.44$):** Total financial liability = **\$34,700** (Catches 79.6% of churners).
* **Net Business Value:** The model saves **\$152,300** compared to no intervention, and threshold optimization delivers an additional **\$19,250** in direct cost reduction.

---

### 4. Technical Limitations & Operational Risks

1. **Static Snapshot Limitation:** The dataset provides a cross-sectional snapshot without time-series transaction histories, clickstream event telemetry, or customer service ticketing logs.
2. **Post-Intervention Feedback Loops:** Repeatedly targeting high-risk subscribers with discounts could train consumers to threaten cancellation to receive price concessions.
3. **Data Freshness / Model Drift:** Telecom pricing plans and competitor promotions evolve rapidly; the model requires quarterly retraining on refreshed cohort data.

---

### 5. Responsible AI, Ethics & Fairness

* **Protected Demographics:** Demographic features (`gender`, `SeniorCitizen`, `Partner`, `Dependents`) were strictly audited. The model demonstrates near-zero predictive disparity between male and female subscribers (recall gap $< 1.5\%$).
* **Fair Treatment of Senior Citizens:** Senior citizens have higher average churn (38.8%) due to fixed-income sensitivity. Interventions directed toward senior cohorts must prioritize simplified payment methods and accessibility support rather than pushy contract upgrades.
