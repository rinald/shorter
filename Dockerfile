FROM python:3.11-alpine

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create data directory for persistent storage
RUN mkdir -p /app/data

# Copy python files
COPY *.py .

# Set database path to the mounted volume
ENV DATABASE_URL=sqlite:///./data/shorter.db

# Command to run the application
CMD ["fastapi", "run", "main.py"]
