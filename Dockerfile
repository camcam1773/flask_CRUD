FROM python:3.10-alpine

WORKDIR /crud
ADD app.py .
ADD wsgi.py .
ADD requirements.txt .
ADD ./templates templates/
ADD ./tests tests/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

expose 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--access-logfile", "-", "--workers", "3", "wsgi:app"]