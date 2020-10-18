import pandas as pd
import summarizer

summaryLengths = [2, 4, 6]
lengthToDescriptor = {
  2: 'short',
  4: 'medium',
  6: 'long',
}

df = pd.read_csv('content.csv')

numIssues = df.shape[0]
numCandidates = df.shape[1]

# For each issue in the csv
for i in range(numIssues) :
  issue = df['Topic'][i]
  for j in range(1, numCandidates) :
    candidate = list(df)[j]
    content = df.iloc[i, j]
    summary = ''
    isURL = content.startswith('http')
    for k in range(len(summaryLengths)) :
      numSentences = summaryLengths[k]
      lengthDescriptor = lengthToDescriptor.get(numSentences)
      if isURL:
        # summary = summarizer.summary_from_url(content, numSentences)
        summary = 'url'
      else :
        # summary = summarizer.summary_from_text(content, numSentences)
        summary = 'text'
      # Post summary to API
      print('=====================')
      print('Issue: ', issue)
      print('Candidate: ', candidate)
      print('Sentences: ', numSentences)
      print('Length Description: ', lengthDescriptor)
      print(summary)