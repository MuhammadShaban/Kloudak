FROM python:3.6-slim
COPY mysite/start.sh /start.sh
ADD mysite /mysite
WORKDIR /mysite
run apt-get update && apt-get install gcc -y
run pip3.6 install -r requirements.txt
run pip3.6 install daphne
EXPOSE 3000
CMD ["/start.sh"]
