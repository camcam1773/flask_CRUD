FROM python:3.13-alpine

LABEL org.opencontainers.image.source=https://github.com/camcam1773/flask_CRUD
LABEL org.opencontainers.image.description="Flask CRUD"

WORKDIR /crud
COPY app.py .
COPY wsgi.py .
COPY requirements.txt .
COPY ./templates templates/
COPY ./tests tests/

RUN pip install --upgrade pip setuptools && pip install -r requirements.txt

EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--access-logfile", "-", "--workers", "3", "wsgi:app"]
