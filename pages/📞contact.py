import streamlit as st
st.set_page_config(page_title="🦷 Zoe Dental", layout="wide")

st.markdown("""
<h1 style="color: #c1713b; font-size: 36px; margin-bottom: 20px;">
    📨 Get in touch with Me!
</h1>
""", unsafe_allow_html=True)

    # Contact form ka HTML
contact_form = """
    <form action="https://formsubmit.co/zohakhan11004@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Enter your name" required>
        <input type="email" name="email" placeholder="Enter your email" required>
        <textarea name="message" placeholder="Your Message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    # Form ko display karne ke liye st.markdown ka istemal
st.markdown(contact_form, unsafe_allow_html=True)

    # Form ke styling ke liye CSS
st.markdown("""
    <style>
        form {
            display: flex;
            flex-direction: column;
            justify-content:center;
            align_items:center;
            gap: 15px;
            max-width: 600px;
            margin: 0;  /* Center-align ko remove karen */
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        input, textarea {
            padding: 12px;
            border: 1px solid #c1713b;
            border-radius: 5px;
            font-size: 16px;
            color: #333333;
            background-color: #f8f9fa;
        }
        input::placeholder, textarea::placeholder {
            color: #999999;
        }
        button {
            background-color: #c1713b;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #a65c2e;
        }
    </style>
    """, unsafe_allow_html=True)
