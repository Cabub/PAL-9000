FROM python:3.9-buster
RUN apt-get update && apt-get install -y zip
WORKDIR /app
COPY requirements.txt .
COPY src .
COPY package.sh .
CMD ["./package.sh"]
