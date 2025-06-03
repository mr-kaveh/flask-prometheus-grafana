FROM python:3.9.22-alpine3.22

WORKDIR /app

COPY app.py /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
