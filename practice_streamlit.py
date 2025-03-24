# import streamlit as st
# import requests

# API_URL = "http://127.0.0.1:8000/chat/"  # Ensure FastAPI is running

# st.set_page_config(page_title="🔥 LLAMA AI Chatbot 🔥")

# st.title("🔥 LLAMA AI Chatbot 🔥")

# # Store chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat history
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # Input field
# user_input = st.chat_input("Type your message here...")

# if user_input:
#     # Display user message
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Send request to FastAPI
#     response = requests.post(API_URL, json={"message": user_input})

#     if response.status_code == 200:
#         data = response.json()
#         bot_reply = data.get("response", "No response received.")  # Ensure correct key
#     else:
#         bot_reply = f"Error: {response.status_code} - {response.text}"

#     # Display bot response
#     st.session_state.messages.append({"role": "assistant", "content": bot_reply})
#     with st.chat_message("assistant"):
#         st.markdown(bot_reply)
