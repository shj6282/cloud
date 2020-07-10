import requests
from bs4 import BeautifulSoup

def get_detail(url):
  company = url.find("h3").string
  job = url.find("h2").string
  href = url.find("a",{"class":"preventLink"})["href"]
  return {"href":href,"job":job,"company":company}

def get_remoteok_data(url):
  jobs = []
  result = requests.get(url)
  soup = BeautifulSoup(result.text,"html.parser")
  results = soup.find("table",{"id":"jobsboard"}).find_all("tr",{"class":"job"})
  for i in results:
    jobs.append(get_detail(i))
  return jobs

