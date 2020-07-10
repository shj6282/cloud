import requests
from flask import Flask, render_template, request,redirect,send_file
from SO import get_SO_data
from Remote import get_Remote_data
from remoteok import get_remoteok_data
from exporter import save_to_file
import os

os.system("clear")

db = {}
app = Flask("h22jln")
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/find")
def find():
  word = request.args.get('word').lower()
  if not word:
    return redirect("/")
  if db.get(word):
    SOjobs = db.get(word).get('SO')
    Remotejobs = db.get(word).get('remote')
    remoteokJobs = db.get(word).get('reok')
  else:
    SOurl = f"https://stackoverflow.com/jobs?r=true&q={word}"
    RemoteUrl = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    url = f"https://remoteok.io/remote-dev+{word}-jobs" 
    SOjobs = get_SO_data(SOurl)
    Remotejobs = get_Remote_data(RemoteUrl)
    remoteokJobs = get_remoteok_data(url)
    db[word] = {"SO":SOjobs,"remote":Remotejobs,"reok":remoteokJobs}
  num = len(SOjobs)+len(remoteokJobs)+len(Remotejobs)
  return render_template("find.html",word = word,so = SOjobs,remote=Remotejobs,reok = remoteokJobs,num=num)
   
app.run(host="0.0.0.0")
