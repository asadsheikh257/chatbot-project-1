import streamlit as st
import requests

API_URL = "https://chatbot-project-1-production.up.railway.app/chat/"  # Adjust if running FastAPI on a different host






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



# st.title("LLAMA AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message here...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = requests.post(API_URL, json={"message": user_input})
    # response = requests.post(f"{API_URL}/chat", json={"message": user_input})
    

    if response.status_code == 200:
        bot_reply = response.json()["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        with st.chat_message("assistant"):
            st.write(bot_reply)
    else:
        st.error(f"API Error {response.status_code}: {response.text}")
