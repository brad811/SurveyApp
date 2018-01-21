import MySQLdb
import time
import sys
import getopt
import os

host = os.environ['DB_HOST']
user = os.environ['DB_USER']
password = os.environ['DB_PASS']
port = 3306
db = os.environ['DB_NAME']

try:
  conn = MySQLdb.connect(host=host, user=user, passwd=password, port=port)
  conn.close()
  print("true")
except:
  print("false")
