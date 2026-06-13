import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.health_agent import analyze_health
from agents.milk_agent import analyze_milk_production
from agents.feed_agent import optimize_feed

# Page config
st.set_page_config(
    page_title="Cattle Farm AI",
    page_icon="🐄",
    layout="wide"
)

# Header
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h1 style='color: #4CAF50;'>🐄 AI Cattle Farm Management System</h1>
    <p style='color: #888;'>Powered by LLaMA 3.3 70B • Multi-Agent AI System</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# API Key
api_key = st.sidebar.text_input(
    "🔑 Enter Groq API Key",
    type="password",
    help="Get free key at console.groq.com"
)

st.sidebar.divider()
st.sidebar.markdown("### 📊 Quick Stats")
st.sidebar.metric("AI Agents", "3 Active")
st.sidebar.metric("Model", "LLaMA 3.3 70B")

# Input form
st.markdown("### 🐄 Enter Cow Details")

col1, col2, col3 = st.columns(3)

with col1:
    cow_id = st.text_input("🏷️ Cow ID", placeholder="e.g. COW-001")
    age = st.number_input("📅 Age (years)", min_value=1, max_value=20, value=4)
    breed = st.selectbox("🐄 Breed", [
        "Holstein Friesian",
        "Jersey",
        "Gir",
        "Sahiwal",
        "Murrah Buffalo",
        "HF Cross"
    ])
    weight = st.number_input("⚖️ Weight (kg)", min_value=100, max_value=800, value=400)

with col2:
    temperature = st.number_input("🌡️ Body Temperature (°C)", 
                                   min_value=35.0, max_value=42.0, value=38.5)
    milk_today = st.number_input("🥛 Milk Today (liters)", 
                                  min_value=0.0, max_value=50.0, value=12.0)
    milk_average = st.number_input("📈 Average Milk (liters)", 
                                    min_value=0.0, max_value=50.0, value=14.0)
    milk_last_7_days = st.number_input("📊 Last 7 Days Total (liters)", 
                                        min_value=0.0, max_value=350.0, value=95.0)

with col3:
    symptoms = st.text_area("🤒 Symptoms / Observations", 
                             placeholder="e.g. reduced appetite, limping, nasal discharge",
                             height=100)
    pregnancy_status = st.selectbox("🤰 Pregnancy Status", [
        "Not Pregnant",
        "Pregnant - 1st trimester",
        "Pregnant - 2nd trimester", 
        "Pregnant - 3rd trimester",
        "Recently Calved"
    ])
    current_feed = st.number_input("🌾 Current Feed (kg/day)", 
                                    min_value=1.0, max_value=30.0, value=15.0)
    last_vaccination = st.text_input("💉 Last Vaccination", 
                                      placeholder="e.g. FMD - 3 months ago")

st.divider()

if st.button("🤖 Analyze Cow with AI Agents", use_container_width=True, type="primary"):
    if not api_key:
        st.error("⚠️ Please enter your Groq API Key in the sidebar!")
    elif not cow_id:
        st.error("⚠️ Please enter a Cow ID!")
    elif not symptoms:
        st.error("⚠️ Please enter symptoms or observations!")
    else:
        cow_data = {
            "cow_id": cow_id,
            "age": age,
            "breed": breed,
            "weight": weight,
            "temperature": temperature,
            "milk_today": milk_today,
            "milk_average": milk_average,
            "milk_last_7_days": milk_last_7_days,
            "symptoms": symptoms,
            "pregnancy_status": pregnancy_status,
            "current_feed": current_feed,
            "last_vaccination": last_vaccination
        }

        st.markdown("### 🤖 AI Agent Analysis Results")
        
        col1, col2, col3 = st.columns(3)

        with col1:
            with st.spinner("🏥 Health Agent analyzing..."):
                health_result = analyze_health(cow_data, api_key)
            st.markdown(f"""
            <div style='background: #1e1e2e; padding: 15px; border-radius: 10px;
                        border-top: 3px solid #ff4444;'>
                <h4 style='color: #ff4444;'>🏥 Health Monitor Agent</h4>
                <p style='color: #e0e0e0; font-size: 13px;'>{health_result['analysis']}</p>
            </div>
            """, unsafe_allow_html=True)
            # Send Telegram alert if CRITICAL or SICK
            if "CRITICAL" in health_result['analysis'] or "SICK" in health_result['analysis']:
                try:
                    import requests
                    from datetime import datetime
                    alert_data = {
                        "cow_id": cow_data['cow_id'],
                        "health_status": "CRITICAL",
                        "disease": health_result['analysis'][:100],
                        "action": "Immediate veterinary attention required",
                        "vet_required": "YES",
                        "farm_name": "My Cattle Farm",
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    n8n_url = st.secrets.get("N8N_WEBHOOK_URL", "")
                    requests.post(n8n_url, json=alert_data)
                    st.warning("🚨 CRITICAL ALERT SENT TO FARMER VIA TELEGRAM!")
                except:
                    pass
        with col2:
            with st.spinner("🥛 Milk Agent analyzing..."):
                milk_result = analyze_milk_production(cow_data, api_key)
            st.markdown(f"""
            <div style='background: #1e1e2e; padding: 15px; border-radius: 10px;
                        border-top: 3px solid #0ea5e9;'>
                <h4 style='color: #0ea5e9;'>🥛 Milk Production Agent</h4>
                <p style='color: #e0e0e0; font-size: 13px;'>{milk_result['analysis']}</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            with st.spinner("🌾 Feed Agent calculating..."):
                feed_result = optimize_feed(cow_data, api_key)
            st.markdown(f"""
            <div style='background: #1e1e2e; padding: 15px; border-radius: 10px;
                        border-top: 3px solid #10b981;'>
                <h4 style='color: #10b981;'>🌾 Feed Optimizer Agent</h4>
                <p style='color: #e0e0e0; font-size: 13px;'>{feed_result['analysis']}</p>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
st.markdown("### 💉 Vaccination Reminder System")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Add Vaccination Record")
    vac_cow_id = st.text_input("🏷️ Cow ID", key="vac_cow_id")
    vaccine_name = st.selectbox("💉 Vaccine Name", [
        "FMD (Foot and Mouth Disease)",
        "BQ (Black Quarter)",
        "HS (Haemorrhagic Septicaemia)",
        "Anthrax",
        "Brucellosis",
        "Theileriosis",
        "Rabies"
    ])
    last_given = st.date_input("📅 Last Given Date")
    
    # Calculate next due date
    vaccine_intervals = {
        "FMD (Foot and Mouth Disease)": 6,
        "BQ (Black Quarter)": 12,
        "HS (Haemorrhagic Septicaemia)": 12,
        "Anthrax": 12,
        "Brucellosis": 12,
        "Theileriosis": 12,
        "Rabies": 12
    }
    
    import datetime
    months = vaccine_intervals[vaccine_name]
    next_due = last_given + datetime.timedelta(days=months*30)
    today = datetime.date.today()
    days_remaining = (next_due - today).days
    
    if st.button("➕ Check Vaccination Status"):
        if days_remaining < 0:
            st.error(f"⚠️ OVERDUE! {vaccine_name} was due {abs(days_remaining)} days ago!")
        elif days_remaining < 30:
            st.warning(f"⏰ Due soon! {vaccine_name} due in {days_remaining} days on {next_due}")
        else:
            st.success(f"✅ OK! Next {vaccine_name} due on {next_due} ({days_remaining} days remaining)")

with col2:
    st.markdown("#### 📅 Vaccination Schedule")
    st.markdown("""
    | Vaccine | Frequency | Notes |
    |---------|-----------|-------|
    | FMD | Every 6 months | Most important! |
    | BQ | Yearly | Young cattle |
    | HS | Yearly | Monsoon season |
    | Anthrax | Yearly | High risk areas |
    | Brucellosis | Once | Female calves |
    | Theileriosis | Once | Tick prone areas |
    """)
    st.divider()
st.markdown("### 📈 Milk Production Tracker")

import plotly.graph_objects as go
import random

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Enter Last 7 Days Production")
    days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    milk_values = []
    
    for i, day in enumerate(days):
        val = st.number_input(f"{day} (liters)", 
                             min_value=0.0, 
                             max_value=50.0, 
                             value=float(14 - i*0.5),
                             key=f"milk_{i}")
        milk_values.append(val)

with col2:
    st.markdown("#### 📊 Production Chart")
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=days,
        y=milk_values,
        mode='lines+markers',
        name='Daily Production',
        line=dict(color='#0ea5e9', width=3),
        marker=dict(size=10, color='#0ea5e9')
    ))
    
    # Average line
    avg = sum(milk_values) / len(milk_values)
    fig.add_hline(
        y=avg, 
        line_dash="dash", 
        line_color="#ff4444",
        annotation_text=f"Average: {avg:.1f}L"
    )
    
    fig.update_layout(
        plot_bgcolor='#1e1e2e',
        paper_bgcolor='#1e1e2e',
        font=dict(color='white'),
        xaxis=dict(gridcolor='#333'),
        yaxis=dict(gridcolor='#333', title='Liters'),
        title='7-Day Milk Production',
        height=300
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Stats
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Average", f"{avg:.1f}L")
    col_b.metric("Highest", f"{max(milk_values):.1f}L")
    col_c.metric("Lowest", f"{min(milk_values):.1f}L")
    st.divider()
st.markdown("### 💰 Profit Calculator per Cow")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📥 Income")
    milk_price = st.number_input("💵 Milk Price (₹ per liter)", 
                                  min_value=20, max_value=100, value=35)
    daily_milk = st.number_input("🥛 Daily Milk (liters)", 
                                  min_value=0.0, max_value=50.0, value=12.0,
                                  key="profit_milk")
    other_income = st.number_input("💰 Other Income per month (₹)", 
                                    min_value=0, value=500,
                                    help="Calf sale, dung etc")

with col2:
    st.markdown("#### 📤 Expenses")
    feed_cost = st.number_input("🌾 Feed Cost per day (₹)", 
                                 min_value=0, max_value=1000, value=250)
    medicine_cost = st.number_input("💊 Medicine per month (₹)", 
                                     min_value=0, value=300)
    labor_cost = st.number_input("👨‍🌾 Labor per month (₹)", 
                                  min_value=0, value=1500)
    other_expense = st.number_input("📦 Other expenses per month (₹)", 
                                     min_value=0, value=200)

if st.button("💰 Calculate Profit", use_container_width=True):
    # Monthly calculations
    monthly_milk_income = daily_milk * 30 * milk_price
    total_income = monthly_milk_income + other_income
    
    total_expense = (feed_cost * 30) + medicine_cost + labor_cost + other_expense
    
    profit = total_income - total_expense
    profit_per_day = profit / 30

    # Display results
    st.markdown("#### 📊 Monthly Financial Report")
    
    col_a, col_b, col_c = st.columns(3)
    
    col_a.metric(
        "Total Income", 
        f"₹{total_income:,.0f}",
        f"Milk: ₹{monthly_milk_income:,.0f}"
    )
    col_b.metric(
        "Total Expense", 
        f"₹{total_expense:,.0f}",
        f"Feed: ₹{feed_cost*30:,.0f}"
    )
    col_c.metric(
        "Net Profit", 
        f"₹{profit:,.0f}",
        f"₹{profit_per_day:.0f}/day"
    )
    
    # Profit bar
    if profit > 0:
        st.success(f"✅ This cow is PROFITABLE! Making ₹{profit:,.0f} per month!")
    elif profit == 0:
        st.warning("⚠️ Breaking even — no profit no loss!")
    else:
        st.error(f"❌ This cow is LOSING ₹{abs(profit):,.0f} per month! Take action!")
    
    # Breakdown chart
    fig2 = go.Figure(data=[
        go.Bar(name='Income', x=['Monthly'], y=[total_income], 
               marker_color='#10b981'),
        go.Bar(name='Expense', x=['Monthly'], y=[total_expense], 
               marker_color='#ff4444'),
        go.Bar(name='Profit', x=['Monthly'], y=[profit], 
               marker_color='#0ea5e9')
    ])
    
    fig2.update_layout(
        plot_bgcolor='#1e1e2e',
        paper_bgcolor='#1e1e2e',
        font=dict(color='white'),
        barmode='group',
        height=250,
        title='Income vs Expense vs Profit'
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    