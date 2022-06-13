FROM python:3.8-slim-buster

RUN apt-get update
RUN apt-get install wget -y

RUN which python
RUN python --version

# Source folder
WORKDIR /app
# Install dependences
ADD requirements.txt /app/src/requirements.txt
RUN pip install -r /app/src/requirements.txt

# Add source code
ADD src /app/src
ADD docker/exec.sh /app

EXPOSE 8000

ENV PYTHONPATH=/app:/app/src

CMD ["./exec.sh"]
