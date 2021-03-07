FROM ubuntu:20.04

WORKDIR /root

RUN apt-get update \
    && apt-get -y install \
        build-essential \
        python3 \
        wget \
    && wget https://www.openssl.org/source/old/1.0.1/openssl-1.0.1f.tar.gz \
        https://archive.apache.org/dist/httpd/httpd-2.2.34.tar.gz \
    && tar xvf openssl-1.0.1f.tar.gz \
    && tar xvf httpd-2.2.34.tar.gz \
    && cd /root/openssl-1.0.1f \
    && ./config shared \
    && make \
    && make install_sw \
    && cd /root/httpd-2.2.34 \
    && ./configure --enable-ssl --with-ssl=/usr/local/ssl \
    && make \
    && make install \
    && cd /root \
    && apt-get clean \
    && rm -rf *

WORKDIR /usr/local/apache2/

COPY httpbin cgi-bin/httpbin

RUN chmod +x cgi-bin/httpbin \
    && sed 's/#ServerName www.example.com:80/ServerName www.example.com:80/g' conf/httpd.conf -i \
    && sed 's/#Include conf\/extra\/httpd-ssl.conf/Include conf\/extra\/httpd-ssl.conf/g' conf/httpd.conf -i \
    && openssl req -x509 -nodes -days 30 -newkey rsa:2048 -keyout conf/server.key -out conf/server.crt -subj "/CN= www.example.com"

CMD LD_LIBRARY_PATH=/usr/local/ssl/lib bin/apachectl -k start && tail -f logs/access_log
