FROM python:3.11-slim

# Install Java (required by Spark)
RUN apt-get update && \
    apt-get install -y --no-install-recommends default-jre-headless procps && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=3000
EXPOSE 3000
CMD ["python", "app.py"]   # or your entrypoint