import streamlit as st

# 1. Professional Page Configuration
st.set_page_config(page_title="Vicky Data Solutions | Business Software Suite", layout="wide", initial_sidebar_state="expanded")

# 2. Modern UI Overrides (Forces sidebar to show up correctly and cleans the interface)
st.markdown("""
    <style>
    /* Completely hide default Streamlit footer and deploy menus */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Make sure the header bar and sidebar toggle icon are fully visible and clickable */
    header {visibility: visible !important; background-color: transparent !important;}
    div[data-testid="stSidebarCollapse"] {visibility: visible !important; display: block !important; left: 10px !important;}
    
    /* Clean up the native sidebar appearance to look premium */
    section[data-testid="stSidebar"] {
        background-color: #f8f9fa;
        border-right: 1px solid #e0e0e0;
    }
    section[data-testid="stSidebar"] .stMarkdown h2 {
        color: #003366 !important;
        font-size: 1.2rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Hero Section (Company Branding)
st.markdown("""
    <div style="text-align: center; padding: 40px 0;">
        <h1 style="color: #003366; font-size: 3em; margin-bottom: 10px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">Vicky Data Solutions</h1>
        <h3 style="color: #4a4a4a; font-weight: normal; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">Enterprise-Grade Operational Software & Automation</h3>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 4. Software Showcase Section Title
st.markdown("<h2 style='text-align: center; color: #111; margin-bottom: 30px; font-family: sans-serif;'>Our Custom Software Deployments</h2>", unsafe_allow_html=True)

# 5. Three-Column Layout for Your Real Projects
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📦 Inventory Management")
    st.write("Real-time stock tracking, automated reorder level triggers, dynamic transaction logging, and professional tax invoice generation.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Clicking this button will now toggle an inline message right where they are looking
    if st.button("Launch Inventory App", key="inv_btn", use_container_width=True):
        st.warning("👈 Please look at the very top-left side of your screen. Click the small **'>' arrow icon** to open the sidebar panel and click on **1_Inventory**!")

with col2:
    st.markdown("### 🔍 QR Attendance System")
    st.write("Contactless, secure workforce tracking using dynamic QR code generation, instant scan logging, and automated daily dashboard reporting.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("Launch Attendance Software 🌐", "https://your-attendance-app.streamlit.app", use_container_width=True)

with col3:
    st.markdown("### 🏥 Hospital Management")
    st.write("Centralized healthcare administration portal for tracking doctor availability, patient check-ins, automated bed allocation, and billing.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("Launch Hospital Software 🌐", "https://your-hospital-app.streamlit.app", use_container_width=True)

st.write("---")

# 6. Action / Lead Generation Section
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h3 style='color: #222;'>Need a Custom Software Solution for Your Business?</h3>
        <p style='color: #666;'>We build tailored databases, tracking systems, and automation pipelines designed for local operations.</p>
    </div>
""", unsafe_allow_html=True)

# 7. Layout to center the contact details
_, center_col, _ = st.columns([1, 1, 1])
with center_col:
    if st.button("Get in Touch / Request Quote", use_container_width=True):
        st.success("📩 Contact Vinay Kumar at **9989377136** to schedule a live system demonstration.")

# 8. Professional Footer
st.markdown("""
    <div style="text-align: center; color: #888; font-size: 0.85em; margin-top: 60px; border-top: 1px solid #eee; padding-top: 20px;">
        © 2026 Vicky Data Solutions | Proprietary Business Applications | Bengaluru, KA
    </div>
""", unsafe_allow_html=True)
