from flask import Flask, jsonify
from db import get_summary

app = Flask(__name__)

@app.route('/get-summary/<string:candidate>/<string:issue>/<string:length>')
def summary_route(candidate, issue, length):
  return get_summary(candidate, issue, length)

if __name__ == '__main__':
  app.run()