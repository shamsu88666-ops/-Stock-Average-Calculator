import streamlit as st

# ------------------ APP CONFIG ------------------
st.set_page_config(
    page_title="Stock Average Calculator",
    page_icon="📈",
    layout="centered"
)

# ------------------ TITLE ------------------
st.title("📈 Stock Average Calculator")
st.write("Developed by: **shamsudeen abdulla**")
st.link_button("Contact Developer", "https://www.facebook.com/shamsudeen.abdulla.2025/")
st.caption("A simple tool to calculate stock average price and target averaging quantity")

st.divider()

# =================================================
# FEATURE 1 : AVERAGE PRICE CALCULATION
# =================================================
st.subheader("1️⃣ Calculate Average Buy Price")

col1, col2 = st.columns(2)

with col1:
    qty1 = st.number_input("First Purchase Quantity", min_value=0, step=1)
    price1 = st.number_input("First Purchase Price", min_value=0.0, step=0.01)

with col2:
    qty2 = st.number_input("Second Purchase Quantity", min_value=0, step=1)
    price2 = st.number_input("Second Purchase Price", min_value=0.0, step=0.01)

if st.button("Calculate Average Price"):
    total_qty = qty1 + qty2
    total_amount = (qty1 * price1) + (qty2 * price2)

    if total_qty > 0:
        avg_price = total_amount / total_qty

        st.success("Calculation Result")
        st.write(f"**Total Quantity:** {total_qty}")
        st.write(f"**Total Invested Amount:** ₹ {total_amount:,.2f}")
        st.write(f"**Average Buy Price:** ₹ {avg_price:,.2f}")
    else:
        st.warning("Total quantity must be greater than zero")

st.divider()

# =================================================
# FEATURE 2 : TARGET AVERAGE CALCULATION
# =================================================
st.subheader("2️⃣ Quantity Required for Target Average Price")

col3, col4 = st.columns(2)

with col3:
    existing_qty = st.number_input("Existing Quantity", min_value=0, step=1, key="eq")
    existing_price = st.number_input("Existing Buy Price", min_value=0.0, step=0.01, key="ep")

with col4:
    current_price = st.number_input("Current Market Price", min_value=0.0, step=0.01)
    target_avg = st.number_input("Desired Average Price", min_value=0.0, step=0.01)

if st.button("Calculate Required Quantity"):
    invested_amount = existing_qty * existing_price

    if current_price != target_avg:
        required_qty = (target_avg * existing_qty - invested_amount) / (current_price - target_avg)

        if required_qty > 0:
            required_amount = int(required_qty) * current_price
            st.success("Calculation Result")
            st.write(f"**Quantity Required to Buy:** {int(required_qty)}")
            st.write(f"**Total Amount Required:** ₹ {required_amount:,.2f}")
        else:
            st.warning("Target average is not achievable at this price")
    else:
        st.warning("Current price and target average cannot be the same")

# ------------------ FOOTER ------------------
st.divider()
st.caption("⚠️ For educational purposes only | Market risks apply")
