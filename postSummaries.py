import pandas as pd
import summarizer
import requests
import time
import json

def post_request(cid, candidate, issue, summaries, source):
  headers = {
    'Content-Type': 'application/json'
  }

  url = "https://tensile-pixel-272123.wl.r.appspot.com/"
  url += "post-summary/"
  url += str(candidate) + '/'
  url += str(issue) + '/'
  url += str(cid)

  print('Request: ' + url+ '\n')
  data = {
    'short': summaries[0],
    'medium': summaries[1],
    'long': summaries[2],
    'url': source
  }
  result = requests.request("Post", url, headers=headers, data=json.dumps(data))
  print(result.text)

summaryLengths = [2, 4, 6]
candidates = ['Trump', 'Biden']
lengthToDescriptor = {
  2: 'short',
  4: 'med',
  6: 'long',
}

df = pd.read_csv('content.csv')

numIssues = df.shape[0]
numCandidates = df.shape[1]

# For each issue in the csv
for i in range(numIssues) :
  issue = df['Topic'][i]

  for j in range(2, numCandidates) :
    summaries = []
    candidate = list(df)[j]
    source = df.iloc[i, j]
    isURL = source.startswith('http')

    if not isURL:
      partition = source.partition('\n')
      source = 'https://' + partition[0]
      text = partition[2]

    for k in range(len(summaryLengths)) :
      numSentences = summaryLengths[k]
      if isURL:
        summary = summarizer.summary_from_url(source, numSentences)
      else :
        summary = summarizer.summary_from_text(text, numSentences)
      # Post summary to API
      print('=====================')
      print('Issue: ', issue)
      print('Candidate: ', candidate)
      # print(summary)
      summaries.append(summary)

    post_request(i * 2 + j, candidates[j-1], issue, summaries, source)




