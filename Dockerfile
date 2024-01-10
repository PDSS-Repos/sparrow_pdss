FROM python:3.10

ADD sparrow-data/donut/requirements.txt /opt/requirements.txt
RUN pip install -U pip
RUN pip install -r /opt/requirements.txt

RUN apt-get update
RUN apt-get install poppler-utils -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install torch torchvision torchaudio
RUN pip install python-doctr

ADD sparrow-data /opt/sparrow-data
ADD sparrow-ui  /opt/sparrow-ui

WORKDIR /opt