FROM node:20.10-alpine3.19 AS builder
RUN apk add git
WORKDIR /web
RUN git clone https://github.com/alvarocastilla05/FilimuFy .
RUN npm install -g @angular/cli
RUN cd App-FilimuFy && npm install
RUN cd App-FilimuFy ng build --configuration production --aot

FROM nginx:alpine
WORKDIR /web
COPY --from=builder /web/dist/App-FilimuFy/* .
RUN mv ./* /usr/share/nginx/html/