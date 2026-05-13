# Start from official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for faster rebuilds)
COPY requirements.txt .

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your project files
COPY . .

# Tell Docker which port Streamlit uses
EXPOSE 8501

# Command to run your app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]