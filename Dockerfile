FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD wait_for_mysql.py /tmp/
RUN pip install -r requirements.txt
ADD . /code/
