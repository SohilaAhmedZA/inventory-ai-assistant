import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_BASE = "http://localhost:8000"

st.set_page_config(
    page_title="Inventory AI Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("🤖 Inventory AI Assistant")
st.sidebar.markdown("AI-powered inventory analytics")
page = st.sidebar.radio("Navigation", ["Dashboard", "AI Chat"])

# ---------------------------
# Dashboard Page
# ---------------------------
if page == "Dashboard":

    st.title("📊 Inventory Dashboard")

    # KPI Section
    response = requests.get(f"{API_BASE}/inventory-summary")
    data = response.json()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Customers", data["customers"])
    col2.metric("Vendors", data["vendors"])
    col3.metric("Items", data["items"])
    col4.metric("Orders", data["sales_orders"])

    st.markdown("---")

    # AI Overview
    st.subheader("🧠 AI Business Overview")

    if st.button("Generate AI Insight"):
        ai_res = requests.get(f"{API_BASE}/ai-inventory-overview")
        ai_data = ai_res.json()

        st.success(ai_data["ai_explanation"])

    st.markdown("---")

    # Charts Section
    st.subheader("📈 Inventory Charts")

    chart_data = pd.DataFrame({
        "Category": ["Customers", "Vendors", "Items", "Orders"],
        "Count": [
            data["customers"],
            data["vendors"],
            data["items"],
            data["sales_orders"]
        ]
    })

    fig = px.bar(chart_data, x="Category", y="Count", title="Inventory Distribution")
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# AI Chat Page
# ---------------------------
if page == "AI Chat":

    st.title("💬 Ask Inventory AI")

    question = st.text_input("Ask a business question")

    if st.button("Ask AI"):
        response = requests.get(f"{API_BASE}/ask-ai", params={"question": question})
        answer = response.json()

        st.markdown("### 🤖 AI Answer")
        st.write(answer["answer"])