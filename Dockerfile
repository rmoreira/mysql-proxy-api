FROM python:2.7.14
RUN pip install flask pymysql

RUN mkdir /app
WORKDIR /app
COPY app.py /app/
EXPOSE 5000
CMD FLASK_APP=app.py flask run --host=0.0.0.0
