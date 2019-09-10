FROM python:3.7-alpine

ADD app.py /
ADD requirements.txt /
ADD base.html /templates
ADD index.html /templates
ADD update.html /templates

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]