import requests
from bs4 import BeautifulSoup

def get_detail(url):
  href = url.find("a",{"class":"s-link"})["href"]
  job = url.find("a",{"class":"s-link"}).string
  company = url.find("h3").find("span").string
  return {"href":href,"job":job,"company":company}

def get_SO_data(url):
  jobs = []
  result = requests.get(url)
  soup = BeautifulSoup(result.text,"html.parser")
  results = soup.find_all("div",{"class":"-job"})
  for i in results:
    jobs.append(get_detail(i))
  return jobs

