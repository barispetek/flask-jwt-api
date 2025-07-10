# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Env
ENV FLASK_APP=run.py

# Run
CMD ["flask", "run", "--host=0.0.0.0"]
