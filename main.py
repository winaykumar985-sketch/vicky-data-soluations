import streamlit as st

# 1. Professional Page Config
st.set_page_config(page_title="Vicky Data Solutions | Professional Analytics", layout="wide")

# 2. Hide Streamlit Branding
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. Hero Section (The "Professional" Look)
st.markdown("""
    <div style="text-align: center; padding: 50px 0;">
        <h1 style="color: #003366; font-size: 3em;">Vicky Data Solutions</h1>
        <h3 style="color: #4a4a4a;">Automating Business Operations through Advanced Data Analytics</h3>
    </div>
""", unsafe_allow_html=True)

# 4. Three-Column Service Showcase
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Excel Automation")
    st.write("Turn manual, time-consuming spreadsheets into automated, error-free reporting systems.")

with col2:
    st.subheader("⚙️ Process Optimization")
    st.write("Streamlining your supply chain and operational data to improve overall business efficiency.")

with col3:
    st.subheader("📈 Custom Dashboards")
    st.write("Data-driven web applications designed to give you real-time insights into your key metrics.")

st.write("---")

# 5. Call to Action (How you get paid)
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h3>Ready to optimize your business operations?</h3>
    </div>
""", unsafe_allow_html=True)

if st.button("Schedule a Free Consultation"):
    st.write("Please reach out at: [Your Professional Email/Phone]")

# 6. Minimalist Footer
st.markdown("""
    <div style="text-align: center; color: #888; font-size: 0.8em; margin-top: 50px;">
        © 2026 Vicky Data Solutions | Professional Data Consultancy | Bengaluru
    </div>
""", unsafe_allow_html=True)
