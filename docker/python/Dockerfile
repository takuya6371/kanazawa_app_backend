FROM python:3.8-buster
RUN mkdir -p /var/www
WORKDIR /var/www
ADD requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uwsgi","--ini","/var/www/flask_api/uwsgi.ini"]
RUN ls
