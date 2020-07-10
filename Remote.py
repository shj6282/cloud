import requests
from bs4 import BeautifulSoup

def get_detail(url):
  href = url.find("a")["href"]
  if url.find("span",{"class":"title"}):
    job = url.find("span",{"class":"title"}).string
  else:
    job = None

  if url.find("span",{"class":"company"}):
    company = url.find("span",{"class":"company"}).string
  else:
    company = None
    
  return {"href":href,"job":job,"company":company}

def get_Remote_data(url):
  jobs = []
  result = requests.get(url)
  soup = BeautifulSoup(result.text,"html.parser")
  results = soup.find("div",{"class":"jobs-container"}).find_all("li")
  for i in results:
      jobs.append(get_detail(i))
  return jobs
  

