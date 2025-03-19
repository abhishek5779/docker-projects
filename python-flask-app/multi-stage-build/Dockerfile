# Stage 1: Build Stage (Installs dependencies)
FROM python:3.9 AS builder

# Set the working directory
WORKDIR /app

# Copy only requirements.txt first (Docker caching optimization)
COPY requirements.txt .

# Install dependencies in a temporary directory
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Final Lightweight Runtime Image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /install /usr/local

# Copy application files
COPY app.py .

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask application
ENTRYPOINT ["python3"]
CMD ["app.py"]