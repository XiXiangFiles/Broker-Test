FROM golang:1.15-alpine3.12
RUN apk update && apk add bash git
RUN apk add vim
RUN cd ..
RUN mkdir consumer
WORKDIR /consumer
ADD producer.go  main.go
ADD go.mod go.mod