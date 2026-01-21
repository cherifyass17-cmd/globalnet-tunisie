FROM python:3.11-slim
WORKDIR /app
COPY contact.py .
RUN pip install --no-cache-dir flask flask-cors
USER 1000
EXPOSE 5002
CMD ["python", "contact.py"]
