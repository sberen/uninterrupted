import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

## opens the connection to the CloudSQL VM
## Code Snipped Source: https://www.smashingmagazine.com/2020/08/api-flask-google-cloudsql-app-engine/
def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
      if os.environ.get('GAE_ENV') == 'standard':
        conn = pymysql.connect(user=db_user, password=db_password,
                               unix_socket=unix_socket, db=db_name,
                               cursorclass=pymysql.cursors.DictCursor
                               )
    except pymysql.MySQLError as e:
        print(e)

    return conn

def get_summary(candidate, issue, length):
  conn = open_connection()
  with conn.cursor() as cursor:
    query = '''SELECT s.{}_summary, s.source, s.scrape_date
               FROM candidates as c, candidate_content as s, issues as i
               WHERE c.id = s.candidate_id AND s.issue_id = i.id
                     AND i.name = '{}' AND c.name = '{}';'''.format(length, issue, candidate)
    print(query)
    result = cursor.execute(query)
    content = cursor.fetchall()
    if result == 1:
      retreived_content = jsonify(content)
    else:
      retreived_content = 'No Content For Specific Individiual'
  conn.close()
  return retreived_content

def post_summary(content_id, candidate_id, issue_id, short_summary, med_summary, long_summary, source):
  conn = open_connection()
  with conn.cursor() as cursor:
    cursor.execute('INSERT INTO candidate_content VALUES ({}, \'{}\', \'{}\', \'{}\', {}, {}, \'{}\', CURDATE())'.format(
      content_id,
      short_summary,
      med_summary,
      long_summary,
      issue_id,
      candidate_id,
      source
      )
    )
  conn.commit()
  conn.close()
