FROM python:3.11-slim

# Install ffmpeg + audio libs
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libopus0 \
    libopus-dev \
    && apt-get clean

WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of project
COPY . .

# Start bot
CMD ["python", "bot.py"]
