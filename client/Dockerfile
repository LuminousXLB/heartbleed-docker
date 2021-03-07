FROM python:alpine3.8

COPY . /root/work

WORKDIR /root/work

RUN pip3 install -r requirement.txt

CMD ["python3", "client.py"]
