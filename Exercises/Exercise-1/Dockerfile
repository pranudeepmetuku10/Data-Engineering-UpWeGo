FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY solution.py .
COPY sample_data/ sample_data/ 2>/dev/null || true

CMD ["python", "solution.py"]
