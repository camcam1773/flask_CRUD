FROM python:3.9-alpine

WORKDIR /crud
ADD app.py .
ADD wsgi.py .
ADD requirements.txt .
ADD ./templates ./templates/

RUN pip install -r requirements.txt

expose 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "3", "wsgi:app"]