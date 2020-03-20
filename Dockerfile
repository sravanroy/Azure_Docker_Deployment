# use python as base image
FROM python


#from alpine:latest

#RUN apk add --no-cache python3-dev \
 #   && pip3 install --upgrade pip

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# open port 5000
EXPOSE 5000

# set env variable

ENV NAME azure

#RUN pip3 --no-cache-dir install -r requirements.txt


CMD ["python", "app.py"]
# use working directory /app

# copy all content of current directory to /app

# installing required packages

 









