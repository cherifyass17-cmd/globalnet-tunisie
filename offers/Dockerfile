FROM python:3.11-slim
WORKDIR /app
COPY offers.py .
RUN pip install --no-cache-dir flask flask-cors
USER 1000
EXPOSE 5000
CMD ["python", "offers.py"]
