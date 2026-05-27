import streamlit as st
import pandas as pd

# Line 5: Page Configuration
st.set_page_config(page_title="Inventory Management System", layout="wide")

# Line 8: Custom Header
st.markdown("""
    <div style="background-color: #003366; padding: 20px; border-radius: 10px; margin-bottom: 25px;">
        <h1 style="color: white; text-align: center; margin: 0;">📦 Smart Inventory Manager</h1>
        <p style="color: #e0e0e0; text-align: center; margin: 5px 0 0 0;">Vicky Data Solutions Enterprise Suite</p>
    </div>
""", unsafe_allow_html=True)

# Line 17: Video Demonstration Placeholder (Ready for tomorrow)
st.subheader("📺 Product Demonstration")
# Replace 'YOUR_VIDEO_LINK_HERE' with your actual link tomorrow (e.g., YouTube or Google Drive video link)
video_link = "YOUR_VIDEO_LINK_HERE" 
if video_link != "YOUR_VIDEO_LINK_HERE":
    st.video(video_link)
else:
    st.info("ℹ️ Product demonstration video will be uploaded here tomorrow.")

st.write("---")

# Line 29: File Uploader Engine
st.subheader("📥 Upload Your Live Database")
uploaded_file = st.file_uploader("Upload your master inventory Excel file (e.g., temp.xlsx)", type=["xlsx"])

# Line 33: Data Logic Execution
if uploaded_file is not None:
    try:
        # Read the Excel sheets directly
        stock_df = pd.read_excel(uploaded_file, sheet_name="Stock")
        tx_df = pd.read_excel(uploaded_file, sheet_name="tranction")
        
        # Clean up unnamed template columns for a professional view
        stock_df = stock_df.loc[:, ~stock_df.columns.str.contains('^Unnamed')]
        
        # Line 43: High-Level Business Metrics Dashboard
        st.subheader("📊 Operational Analytics Dashboard")
        m1, m2, m3 = st.columns(3)
        
        total_products = len(stock_df)
        out_of_stock = len(stock_df[stock_df['Current Stock'] == 0])
        reorder_needed = len(stock_df[stock_df['stock status'] == 'need to buy'])
        
        m1.metric("Total Tracked Items", total_products)
        m2.metric("Critical Out of Stock", out_of_stock, delta=f"-{out_of_stock} items" if out_of_stock > 0 else "0 items", delta_color="inverse")
        m3.metric("Reorder Alerts Active", reorder_needed, delta=f"{reorder_needed} review required" if reorder_needed > 0 else "Clear", delta_color="inverse")
        
        # Line 55: Interactive Tabs for data separation
        tab1, tab2, tab3 = st.tabs(["🛒 Live Stock Registry", "🚨 Critical Reorder Alerts", "📜 Transaction History"])
        
        with tab1:
            st.markdown("#### Master Inventory Records")
            st.dataframe(stock_df, use_container_width=True)
            
        with tab2:
            st.markdown("#### Action Required: Supply Chain Replenishment")
            restock_items = stock_df[stock_df['stock status'] == 'need to buy']
            if not restock_items.empty:
                st.warning("The following items have dropped below their critical safety thresholds:")
                st.dataframe(restock_items[['Product Name', 'Category', 'Current Stock', 'Reorder Level', 'Supplier']], use_container_width=True)
            else:
                st.success("✅ All stock levels are currently stable.")
                
        with tab3:
            st.markdown("#### Automated Transaction Logging")
            st.dataframe(tx_df, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Error compiling spreadsheet data: {e}. Ensure your file contains 'Stock' and 'tranction' sheets.")
else:
    st.warning("👋 Please upload your 'temp.xlsx' file above to access the automated dashboard features.")
