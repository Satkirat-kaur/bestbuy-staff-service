# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Set environment variable
ENV PORT=5000

# Run the application
CMD ["python", "app.py"]
