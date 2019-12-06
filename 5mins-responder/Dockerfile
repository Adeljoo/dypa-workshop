FROM python:alpine3.7
# Added some dependencies for responder
RUN apk add alpine-sdk gcc
# See what I did here? discussion topic
COPY requirements.txt .
RUN pip install -r requirements.txt
# Get the file here
COPY . /app
WORKDIR /app
EXPOSE 5042
CMD python ./index.py