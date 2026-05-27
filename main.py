import streamlit as st
import pandas as pd

# 1. Professional Page Configuration
st.set_page_config(page_title="Vicky Data Solutions | Business Software Suite", layout="wide")

# 2. Hide Default Streamlit Branding
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Initialize a session state to track pages
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Add a "Back to Home" button if inside a module
if st.session_state.current_page != "Home":
    if st.button("⬅️ Back to Main Suite"):
        st.session_state.current_page = "Home"
        st.rerun()

# --- PAGE 1: HOME SUB-SUITE ---
if st.session_state.current_page == "Home":
    st.markdown("""
        <div style="text-align: center; padding: 40px 0;">
            <h1 style="color: #003366; font-size: 3em; margin-bottom: 10px;">Vicky Data Solutions</h1>
            <h3 style="color: #4a4a4a; font-weight: normal;">Enterprise-Grade Operational Software & Automation</h3>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("<h2 style='text-align: center; color: #111; margin-bottom: 30px;'>Our Custom Software Deployments</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📦 Inventory Management")
        st.write("Real-time stock tracking, automated reorder level triggers, dynamic transaction logging, and professional tax invoice generation.")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Launch Inventory App 🚀", key="inv_btn", use_container_width=True):
            st.session_state.current_page = "Inventory"
            st.rerun()

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

    st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h3 style='color: #222;'>Need a Custom Software Solution for Your Business?</h3>
            <p style='color: #666;'>We build tailored databases, tracking systems, and automation pipelines designed for local operations.</p>
        </div>
    """, unsafe_allow_html=True)

    _, center_col, _ = st.columns([1, 1, 1])
    with center_col:
        if st.button("Get in Touch / Request Quote", use_container_width=True):
            st.success("📩 Contact Vinay Kumar at **9989377136** to schedule a live system demonstration.")

    st.markdown("""
        <div style="text-align: center; color: #888; font-size: 0.85em; margin-top: 60px; border-top: 1px solid #eee; padding-top: 20px;">
            © 2026 Vicky Data Solutions | Proprietary Business Applications | Bengaluru, KA
        </div>
    """, unsafe_allow_html=True)

# --- PAGE 2: INVENTORY SYSTEM (CRASH-PROOF VERSION) ---
elif st.session_state.current_page == "Inventory":
    st.markdown("""
        <div style="background-color: #003366; padding: 20px; border-radius: 10px; margin-bottom: 25px;">
            <h1 style="color: white; text-align: center; margin: 0;">📦 Smart Inventory Manager</h1>
            <p style="color: #e0e0e0; text-align: center; margin: 5px 0 0 0;">Vicky Data Solutions Enterprise Suite</p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("📺 Product Demonstration")
    st.info("ℹ️ Product demonstration video will be uploaded here tomorrow.")
    st.write("---")

    st.subheader("📥 Upload Your Live Database")
    uploaded_file = st.file_uploader("Upload your master inventory Excel file (e.g., temp.xlsx)", type=["xlsx"])

    if uploaded_file is not None:
        try:
            # Open the Excel file cleanly
            xl = pd.ExcelFile(uploaded_file)
            sheet_names = xl.sheet_names
            
            # Safe Sheet Loading Logic
            stock_sheet = "Stock" if "Stock" in sheet_names else sheet_names[0]
            stock_df = pd.read_excel(uploaded_file, sheet_name=stock_sheet)
            stock_df = stock_df.loc[:, ~stock_df.columns.str.contains('^Unnamed')]
            
            # Safe Transaction Loading Logic (Prevents IndexError)
            tx_df = None
            if "tranction" in sheet_names:
                tx_df = pd.read_excel(uploaded_file, sheet_name="tranction")
            elif len(sheet_names) > 1:
                tx_df = pd.read_excel(uploaded_file, sheet_name=sheet_names[1])
                
            if tx_df is not None:
                tx_df = tx_df.loc[:, ~tx_df.columns.str.contains('^Unnamed')]
            
            # Dashboard Calculations
            st.subheader("📊 Operational Analytics Dashboard")
            m1, m2, m3 = st.columns(3)
            
            total_products = len(stock_df)
            
            # Find Column Names dynamically or fallback to positions safely
            stock_col = 'Current Stock' if 'Current Stock' in stock_df.columns else (stock_df.columns[4] if len(stock_df.columns) > 4 else stock_df.columns[-1])
            status_col = 'stock status' if 'stock status' in stock_df.columns else (stock_df.columns[7] if len(stock_df.columns) > 7 else stock_df.columns[-1])
            
            # Execute safety counts
            try:
                out_of_stock = len(stock_df[stock_df[stock_col] == 0])
            except:
                out_of_stock = 0
                
            try:
                reorder_needed = len(stock_df[stock_df[status_col].astype(str).str.lower().str.contains('buy|out|no', na=False)])
            except:
                reorder_needed = 0
            
            m1.metric("Total Tracked Items", total_products)
            m2.metric("Critical Out of Stock", out_of_stock, delta=f"-{out_of_stock} items" if out_of_stock > 0 else "0 items", delta_color="inverse")
            m3.metric("Reorder Alerts Active", reorder_needed, delta=f"{reorder_needed} required" if reorder_needed > 0 else "Clear", delta_color="inverse")
            
            # Display Tabs Layout
            tab_labels = ["🛒 Live Stock Registry", "🚨 Critical Reorder Alerts"]
            if tx_df is not None:
                tab_labels.append("📜 Transaction History")
                
            tabs = st.tabs(tab_labels)
            
            with tabs[0]:
                st.markdown("#### Master Inventory Table")
                st.dataframe(stock_df, use_container_width=True)
            with tabs[1]:
                st.markdown("#### Supply Chain Actions")
                try:
                    restock_items = stock_df[stock_df[status_col].astype(str).str.lower().str.contains('buy|out|no', na=False)]
                    if not restock_items.empty:
                        st.dataframe(restock_items, use_container_width=True)
                    else:
                        st.success("✅ All stock levels are currently stable.")
                except:
                    st.info("Upload standard formatted data to filter real-time restock warnings.")
                    
            if tx_df is not None:
                with tabs[2]:
                    st.markdown("#### System Logs")
                    st.dataframe(tx_df, use_container_width=True)
                    
        except Exception as e:
            st.error(f"❌ Layout Parsing Error: {e}. Please ensure you are uploading a valid structured spreadsheet file.")
    else:
        st.warning("👋 Please upload your 'temp.xlsx' file above to access the automated dashboard features.")
