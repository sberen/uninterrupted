import requests
import json

def summary_from_url(url, sentences):
  f = open("key.txt", "r")
  querystring = {
    "key":f.read(),
    "sentences":sentences,
    "url":url
  }
  return summary(querystring)

def summary_from_text(txt, sentences):
  f = open("key.txt", "r")
  querystring = {
    "key":f.read(),
    "sentences":sentences,
    "txt":txt
  }
  return summary(querystring)

def summary(querystring):
  url = "https://api.meaningcloud.com/summarization-1.0"
  response = requests.request("Post", url, headers=None, params=querystring)
  data = json.loads(response.text)

  return(data["summary"])

#Uncomment for sample usage

# txt = """
# Joe Biden believes to his core that there’s no greater economic engine in the world than the hard work and ingenuity of the American people. Nobody has more respect for the working women and men who get up every day to build and sustain this country, or more confidence that they can meet the challenges we face.
# Make no mistake: America has been knocked down. The unemployment rate is higher than it was in the Great Recession. Millions have lost jobs, hours, pay, health care, or the small business they started, through no fault of their own.
# The pandemic has also laid bare some unacceptable truths. Even before COVID-19, the Trump Administration was pursuing economic policies that rewarded wealth over work and corporations over working families. Too many families were struggling to make ends meet and too many parents were worried about the economic future for their children. And, Black and Latino Americans, Native Americans, immigrants, and women have never been welcomed as full participants in the economy.
# Biden believes this is no time to just build back to the way things were before, with the old economy’s structural weaknesses and inequalities still in place. This is the moment to imagine and build a new American economy for our families and the next generation.
# An economy where every American enjoys a fair return for their work and an equal chance to get ahead. An economy more vibrant and more powerful precisely because everybody will be cut in on the deal.
# """
# print(summary_from_text(txt, 5))