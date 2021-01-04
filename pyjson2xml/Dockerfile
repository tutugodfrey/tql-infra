FROM python:3

WORKDIR /usr/src/app

RUN apt update
RUN apt install vim -y

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./encrypt.py ./json2xml.py ./functs.py ./myjson.json ./

# CMD [ "./json2xml.py", "myjson.json" ]
CMD bash

