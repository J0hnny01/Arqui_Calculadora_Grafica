import urllib.request
import zipfile
import os

url = "https://github.com/LogicCircuit/LogicCircuit/archive/refs/heads/master.zip"
urllib.request.urlretrieve(url, "lc.zip")
with zipfile.ZipFile("lc.zip", 'r') as zip_ref:
    zip_ref.extractall("lc")
