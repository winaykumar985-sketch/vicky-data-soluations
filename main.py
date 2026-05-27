import streamlit as st

# Line 4: Professional Page Configuration
st.set_page_config(page_title="Vicky Data Solutions | Business Software Suite", layout="wide")

# Line 7: Hide Default Streamlit Branding
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Line 17: Hero Section (Company Branding)
st.markdown("""
    <div style="text-align: center; padding: 40px 0;">
        <h1 style="color: #003366; font-size: 3em; margin-bottom: 10px;">Vicky Data Solutions</h1>
        <h3 style="color: #4a4a4a; font-weight: normal;">Enterprise-Grade Operational Software & Automation</h3>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# Line 27: Software Showcase Section Title
st.markdown("<h2 style='text-align: center; color: #111; margin-bottom: 30px;'>Our Custom Software Deployments</h2>", unsafe_allow_html=True)

# Line 30: Three-Column Layout for Your Real Projects
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📦 Inventory Management")
    st.write("Real-time stock tracking, automated reorder level triggers, dynamic transaction logging, and professional tax invoice generation.")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Launch Inventory App", key="inv_btn", use_container_width=True):
        st.info("To open this module, select '1_Inventory' from the sidebar menu on the left.")

with col2:
    st.markdown("### 🔍 QR Attendance System")
    st.write("Contactless, secure workforce tracking using dynamic QR code generation, instant scan logging, and automated daily dashboard reporting.")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Launch Attendance App", key="att_btn", use_container_width=True):
        st.info("To open this module, select '2_Attendance' from the sidebar menu on the left.")

with col3:
    st.markdown("### 🏥 Hospital Management")
    st.write("Centralized healthcare administration portal for tracking doctor availability, patient check-ins, automated bed allocation, and billing.")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Launch Hospital App", key="hosp_btn", use_container_width=True):
        st.info("To open this module, select '3_Hospital' from the sidebar menu on the left.")

st.write("---")

# Line 57: Action / Lead Generation Section
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h3 style='color: #222;'>Need a Custom Software Solution for Your Business?</h3>
        <p style='color: #666;'>We build tailored databases, tracking systems, and automation pipelines designed for local operations.</p>
    </div>
""", unsafe_allow_html=True)

# Line 65: Layout to center the contact details
_, center_col, _ = st.columns([1, 1, 1])
with center_col:
    if st.button("Get in Touch / Request Quote", use_container_width=True):
        st.success("📩 Contact Vinay Kumar at **9989377136** to schedule a live system demonstration.")

# Line 71: Professional Footer
st.markdown("""
    <div style="text-align: center; color: #888; font-size: 0.85em; margin-top: 60px; border-top: 1px solid #eee; padding-top: 20px;">
        © 2026 Vicky Data Solutions | Proprietary Business Applications | Bengaluru, KA
    </div>
""", unsafe_allow_html=True)
