FROM python:alpine3.7
# Added some dependencies for responder
RUN apk add openssl alpine-sdk gcc
COPY . /app
WORKDIR /app
# Add C binding for python
RUN pip install -U setuptools pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py