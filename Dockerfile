FROM python:3.9-slim

WORKDIR /app

COPY order_service.py /app

RUN pip install Flask requests

CMD ["python", "order_service.py"]
