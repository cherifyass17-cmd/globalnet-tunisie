FROM python:3.11-slim
WORKDIR /app
COPY auth.py .
RUN pip install --no-cache-dir flask flask-cors
USER 1000
EXPOSE 5001
CMD ["python", "auth.py"]
