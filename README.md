# Mistral AI Chatbot 🤖

🚀 **An AI-powered chatbot built with FastAPI, Streamlit, and Mistral AI!**

---

## 🌟 Overview

Mistral AI Chatbot is an interactive chatbot application that leverages **Mistral AI's models** to generate intelligent responses. The backend is powered by **FastAPI**, while the frontend is built with **Streamlit** for a user-friendly interface. The project is deployed on **Railway**, making it accessible online.

---

## 🔥 Features

✅ **FastAPI Backend** – Efficient API handling for chatbot interactions\
✅ **Streamlit Frontend** – Simple and elegant UI for a great user experience\
✅ **Mistral AI Integration** – Leverages cutting-edge AI models for chat responses\
✅ **Docker Support** – Easily containerized for deployment\
✅ **CORS Enabled** – Seamless communication between frontend and backend\
✅ **Deployed on Railway** – Accessible anywhere with cloud hosting

---

## 🏗️ Tech Stack

- **Backend:** FastAPI 🚀
- **Frontend:** Streamlit 🎨
- **AI Model:** Mistral AI 🤖
- **Deployment:** Railway 🌐
- **Containerization:** Docker 🐳

---

## 🎬 Demo

\
[Live Demo](your-deployment-url) 🔗

---

## 📥 Installation & Setup

Follow these steps to set up the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/mistral-chatbot.git
cd mistral-chatbot
```

### 2️⃣ Create & Activate a Virtual Environment

```bash
python -m venv myenv  # Create virtual environment
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the FastAPI Backend

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 5️⃣ Run the Streamlit Frontend

```bash
streamlit run client.py
```

---

## 🐳 Running with Docker

To containerize and run the project using Docker:

```bash
docker build -t mistral-chatbot .
docker run -p 8000:8000 mistral-chatbot
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description                             |
| ------ | -------- | --------------------------------------- |
| `POST` | `/chat/` | Send a user message and get AI response |

Example request:

```json
{
  "message": "Hello, how are you?"
}
```

Example response:

```json
{
  "choices": [
    {
      "message": {
        "content": "I'm an AI assistant! How can I help you today?"
      }
    }
  ]
}
```

---

## 🚀 Deployment on Railway

1. Push the project to GitHub
2. Connect the repository to **Railway**
3. Set environment variables (API Keys, etc.)
4. Deploy and enjoy! 🎉

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 💡 Future Improvements

- Add authentication for API security 🔐
- Support multiple AI models 🎯
- Enhance UI with better styling 🎨
- Implement chat history storage 📂

---

## 📩 Contact

🔗 **GitHub**: [Asad Abbas Sheikh](https://github.com/asadsheikh257)\
📧 **Email**: [Asad Abbas Sheikh](mailto\:asadsheikh257@gmail.com)\
💼 **LinkedIn**: [Asad Abbas](https://linkedin.com/in/asadabbassheikh)

If you like this project, give it a ⭐ and feel free to contribute! 🚀

