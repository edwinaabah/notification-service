FROM python:3.9-slim

WORKDIR /app

COPY notification_service.py .

RUN pip install flask

EXPOSE 5003

CMD ["python", "notification_service.py"]
