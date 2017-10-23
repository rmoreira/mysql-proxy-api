#!flask/bin/python
from __future__ import print_function
import sys
import os
import pymysql
import json
from flask import Flask, jsonify, request

rds_host  = os.environ['MYSQL_HOST']
name = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
except:
    print("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

def run(query):
  if query == None or query == "":
    return "{\"result\": \"Query string is not valid\"}"

  result = []
  with conn.cursor() as cur:
      cur.execute(query)
      data = cur.fetchall()
      for row in data :
        result.append(row)

  return json.dumps(result)

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def post_query():
    if not request.json or not 'query' in request.json:
        abort(400)
    result = {
        'results': run(request.json['query'])
    }
    return jsonify(result), 200
