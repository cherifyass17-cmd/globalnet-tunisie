FROM python:3.11-slim
WORKDIR /app
COPY *.html .
COPY web-ui.py .
RUN pip install flask flask-cors
EXPOSE 8080
CMD ["python", "web-ui.py"]
