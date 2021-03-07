FROM python:alpine3.8

WORKDIR /root/work

RUN pip3 install --no-cache-dir requests

COPY . /root/work

CMD ["python3", "client.py"]
