FROM python:3.9.5-buster

RUN mkdir /selenium-python
COPY ./requirements.txt /selenium-python
COPY ./setup.py ./setup.py

RUN pip install --upgrade pip
RUN pip install -e .
RUN pip3 install -r /selenium-python/requirements.txt

WORKDIR /selenium-python

CMD "pytest"

# https://stackoverflow.com/a/60797635
ENV PYTHONDONTWRITEBYTECODE=true
