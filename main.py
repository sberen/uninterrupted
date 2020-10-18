from flask import Flask, jsonify, request
from db import get_summary, post_summary

app = Flask(__name__)

ISSUES = {
  "Covid": 1,
  "Climate Change": 2,
  "Immigration": 3,
  "Clean Energy": 4,
  "Foreign Policy": 5,
  "Reopening Schools": 6,
  "National Security": 7,
  "Law Enforcement": 8,
  "Senior Citizens": 9,
  "Education": 10,
  "Economy and Jobs": 11,
  "Veterans": 12
}

CANDIDATES = {
  "Trump": 1,
  "Biden": 2
}
                          ## Donald%20Trump       Covid          med
@app.route('/get-summary/<string:candidate>/<string:issue>/<string:length>')
def get_summary_route(candidate, issue, length):
  return get_summary(candidate, issue, length)

@app.route('/post-summary/<string:candidate>/<string:issue>/<string:content_id>', methods=["POST"])
def post_summary_route(content_id, candidate, issue):
  data = request.get_json()
  print(data)
  post_summary(content_id, CANDIDATES[candidate], ISSUES[issue], data['short'], data['medium'], data['long'], data['url'])
  return "Completed"

if __name__ == '__main__':
  app.run()