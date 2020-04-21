import requests

url = 'https://raw.githubusercontent.com/TheTechRobo/bglugwatch-cleanslate/master/bglug.py'

r = requests.get(url, stream = True)

with open("bglug.py", "wb") as Pypdf:

	for chunk in r.iter_content(chunk_size = 1024):

		if chunk:

			Pypdf.write(chunk)
