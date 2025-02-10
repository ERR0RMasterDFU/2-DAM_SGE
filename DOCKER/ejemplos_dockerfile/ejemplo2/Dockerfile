FROM httpd:2.4-alpine
LABEL maintainer="falla.urdav24@triana.salesianos.edu"
LABEL version="2.0"
RUN apk add git
WORKDIR /web
RUN git clone https://github.com/ERR0RMasterDFU/starWars_api.git .
RUN mv ./* /usr/local/apache2/htdocs/