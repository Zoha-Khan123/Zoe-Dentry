import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="🦷 Zoe Dental", layout="wide")



# # ========================================================= Home ==============================================================


    # Create two columns with equal width and gap
col1, col2 = st.columns(2, gap="medium")  # Columns ke beech mein medium gap
    
with col1:
        # Header aur description
        st.markdown(f"""
        <h1 style="color: #c1713b; font-size: 36px; margin-bottom: 20px;">
            Welcome to Zoe Dental Clinic
        </h1>
        <p style="font-size: 18px; line-height: 1.6; color: #333;">
            At Zoe Dental, we provide the best dental care services to ensure your smile stays bright and healthy. Our team of experienced dentists is here to help you with all your dental needs.
        </p>
        """, unsafe_allow_html=True)
        
        # Button with custom style
        st.markdown("""
        <style>
            .stButton button {
                background-color: #c1713b;
                color: white;
                font-size: 18px;
                padding: 10px 20px;
                border-radius: 5px;
                border: none;
                cursor: pointer;
            }
            .stButton button:hover {
                background-color: #a65c2e;  /* Darker shade for hover */
            }
        </style>
        """, unsafe_allow_html=True)
        st.button("Book Appointment")

with col2:
        # Image with custom styling
        st.markdown("""
        <style>
            .stImage img {
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                width: 200px;
                height:auto;
                object-fit:cover;
                
            }
        </style>
        """, unsafe_allow_html=True)
        st.image("https://clintondentist.net/wp-content/uploads/2023/06/hero-comp.png", caption="Dental Surgeon.", use_container_width=True)













































