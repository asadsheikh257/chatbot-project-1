import streamlit as st

# Custom CSS for fixed title and margin adjustment
st.markdown(
    """
    <style>
    .fixed-title {
        margin-top: 50px; /* Added margin from top */
        position: fixed;
        top: 10px; /* Added margin from top */
        left: 0;
        width: 100%;
        height: 70px;
        background-color: #262730;
        color: white;
        font-size: 26px;
        font-weight: bold;
        text-align: center;
        line-height: 70px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        z-index: 1000;
    }
    
    /* Push Streamlit content down */
    .stApp {
        margin-top: 90px !important; /* Adjusted so content starts lower */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ✅ Fixed Header with Margin
st.markdown('<div class="fixed-title">🔥 LLAMA AI Chatbot 🔥</div>', unsafe_allow_html=True)

# ✅ Content Section
st.write("This is the content of the chatbot. Scroll down and see the title remains fixed.")

# ✅ Add more messages to enable scrolling
for i in range(50):
    st.write(f"Message {i}")
