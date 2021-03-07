FROM ubuntu:14.04

WORKDIR /root

RUN apt-get update \
    && apt-get -y install \
        build-essential \
        wget

RUN wget https://www.openssl.org/source/old/1.0.1/openssl-1.0.1f.tar.gz \
    && tar xvf openssl-1.0.1f.tar.gz \
    && cd openssl-1.0.1f \
    && ./config \
    && make \
    && make install_sw

RUN wget https://archive.apache.org/dist/httpd/httpd-2.2.34.tar.gz \
    && tar xvf httpd-2.2.34.tar.gz \
    && cd httpd-2.2.34 \
    && ./configure \
    && make \
    && make install

RUN apt-get -y install \
        libapache2-mod-php5 \
        php5-cli \
        php5-gd \
        php5-dev \
        php5-json \
        php5-mysql \
    && a2enmod rewrite \
    && a2enmod ssl \
    && a2enmod cgi \
    && a2enmod headers

RUN apt-get clean

CMD /usr/local/apache2/bin/apachectl -k start && tail -f /usr/local/apache2/logs/access_log
