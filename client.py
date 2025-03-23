import streamlit as st
import requests

API_URL = "https://chatbot-project-1-production.up.railway.app/chat/"  # Adjust if running FastAPI on a different host

st.title("Mistral AI Chatbot")

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
