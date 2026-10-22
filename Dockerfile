# Swapping out the vulnerable base image for a secure alpine alternative
FROM python:3.12-alpine

WORKDIR /app

# Install build dependencies if needed (Alpine uses apk instead of apt)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
