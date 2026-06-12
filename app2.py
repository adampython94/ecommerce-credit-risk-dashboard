import streamlit as st

st.set_page_config(page_title="E-Commerce Credit Risk Dashboard")

st.title("E-Commerce Credit Risk Dashboard")

# --------------------------------------------------
# Company Information
# --------------------------------------------------

company = st.text_input(
    "Company Name",
    "Example E-Commerce Ltd"
)

st.subheader(company)

# --------------------------------------------------
# Financial Inputs
# --------------------------------------------------

st.sidebar.header("Financial Information")

revenue = st.sidebar.number_input(
    "Annual Revenue (€)",
    min_value=10000,
    value=1000000,
    step=10000
)

growth = st.sidebar.slider(
    "Revenue Growth (%)",
    -20,
    100,
    15
)

margin = st.sidebar.slider(
    "EBITDA Margin (%)",
    -20,
    50,
    12
)

cash = st.sidebar.number_input(
    "Cash Balance (€)",
    min_value=0,
    value=100000,
    step=10000
)

debt = st.sidebar.number_input(
    "Total Debt (€)",
    min_value=0,
    value=250000,
    step=10000
)

# --------------------------------------------------
# Ratio Calculations
# --------------------------------------------------

debt_ratio = debt / revenue
cash_ratio = cash / revenue

# --------------------------------------------------
# Credit Score
# --------------------------------------------------

score = 50

if growth > 20:
    score += 15

if margin > 10:
    score += 15

if debt_ratio < 0.30:
    score += 10

if cash_ratio > 0.10:
    score += 10

score = min(score, 100)

# --------------------------------------------------
# Risk Rating
# --------------------------------------------------

if score >= 80:
    rating = "Low Risk"
elif score >= 60:
    rating = "Moderate Risk"
else:
    rating = "High Risk"

# --------------------------------------------------
# Funding Logic
# --------------------------------------------------

growth_factor = 1

if growth > 20:
    growth_factor = 1.2
elif growth < 0:
    growth_factor = 0.8

margin_factor = 1

if margin > 15:
    margin_factor = 1.2
elif margin < 5:
    margin_factor = 0.8

leverage_factor = 1

if debt_ratio < 0.2:
    leverage_factor = 1.2
elif debt_ratio > 0.5:
    leverage_factor = 0.7

liquidity_factor = 1

if cash_ratio > 0.15:
    liquidity_factor = 1.1
elif cash_ratio < 0.05:
    liquidity_factor = 0.8

funding = (
    revenue
    * 0.15
    * growth_factor
    * margin_factor
    * leverage_factor
    * liquidity_factor
)

# --------------------------------------------------
# Dashboard Metrics
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Credit Score", score)

with col2:
    st.metric("Risk Rating", rating)

with col3:
    st.metric(
        "Recommended Funding",
        f"€{funding:,.0f}"
    )

# --------------------------------------------------
# Key Ratios
# --------------------------------------------------

st.subheader("Key Ratios")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Debt / Revenue",
        f"{debt_ratio:.2f}x"
    )

with col2:
    st.metric(
        "Cash / Revenue",
        f"{cash_ratio:.2%}"
    )

# --------------------------------------------------
# Credit Assessment
# --------------------------------------------------

st.subheader("Credit Assessment")

growth_status = "Good"
if growth < 0:
    growth_status = "Weak"

margin_status = "Good"
if margin < 5:
    margin_status = "Weak"

leverage_status = "Good"
if debt_ratio > 0.5:
    leverage_status = "Weak"

liquidity_status = "Good"
if cash_ratio < 0.05:
    liquidity_status = "Weak"

if growth_status == "Good":
    st.success(f"Revenue Growth: {growth}%")
else:
    st.error(f"Revenue Growth: {growth}%")

if margin_status == "Good":
    st.success(f"EBITDA Margin: {margin}%")
else:
    st.error(f"EBITDA Margin: {margin}%")

if leverage_status == "Good":
    st.success(f"Debt / Revenue: {debt_ratio:.2f}x")
else:
    st.error(f"Debt / Revenue: {debt_ratio:.2f}x")

if liquidity_status == "Good":
    st.success(f"Cash / Revenue: {cash_ratio:.2%}")
else:
    st.error(f"Cash / Revenue: {cash_ratio:.2%}")

# --------------------------------------------------
# Analyst Commentary
# --------------------------------------------------

st.subheader("Credit Analyst Commentary")

comments = []

if growth > 20:
    comments.append(
        "Strong revenue growth supports increased funding capacity."
    )

if margin > 15:
    comments.append(
        "Business demonstrates strong profitability."
    )

if debt_ratio > 0.5:
    comments.append(
        "Leverage is elevated and should be monitored."
    )

if cash_ratio < 0.05:
    comments.append(
        "Liquidity appears constrained."
    )

if len(comments) == 0:
    comments.append(
        "Business displays a balanced risk profile."
    )

for comment in comments:
    st.write(f"• {comment}")

# --------------------------------------------------
# Stress Test
# --------------------------------------------------

st.subheader("Stress Test")

stress = st.slider(
    "Revenue Decline Scenario (%)",
    0,
    50,
    10
)

stressed_revenue = revenue * (1 - stress / 100)

st.write(
    f"Stressed Revenue: €{stressed_revenue:,.0f}"
)

st.write(
    f"Funding Capacity Under Stress: €{stressed_revenue * 0.15:,.0f}"
)