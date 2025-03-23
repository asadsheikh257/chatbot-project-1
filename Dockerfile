# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI and Streamlit ports
EXPOSE 8000 8501

# Run FastAPI and Streamlit together
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run client.py --server.port 8501 --server.address=0.0.0.0"]
