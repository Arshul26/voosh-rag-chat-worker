# Use slim Python 3.13
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements.txt first for Docker caching
COPY requirements.txt .

# Upgrade pip and install PyTorch CPU version first
RUN pip install --upgrade pip \
    && pip install --no-cache-dir torch==2.8.0

# Install the rest of the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the correct port (match your adapter.py)
EXPOSE 5001

# Run your Flask app
CMD ["python", "adapter.py"]
