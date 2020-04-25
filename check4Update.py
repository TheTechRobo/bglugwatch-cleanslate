# SOURCE: https://likegeeks.com/downloading-files-using-python/
import requests, os

os.remove("bglug.py") #remove bglug.py

url = 'https://raw.githubusercontent.com/TheTechRobo/bglugwatch-cleanslate/master/bglug.py' #url to DL

r = requests.get(url, stream = True) #DL the URL

with open("bglug.py", "wb") as Pypdf:

	for chunk in r.iter_content(chunk_size = 1024):

		if chunk:

			Pypdf.write(chunk) #write 1KB(?) at a time
