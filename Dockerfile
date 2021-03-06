FROM python:3.6.7
MAINTAINER Hilman "hilman@alphatech.id"
RUN mkdir -p /demo
COPY . /demo
RUN pip3 install -r /demo/requirements.txt
WORKDIR /demo
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
