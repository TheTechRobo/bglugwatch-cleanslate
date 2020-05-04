# SOURCE: https://likegeeks.com/downloading-files-using-python/
import requests

url = 'https://thetechrobo.github.io/resources/bglug.py' #url to DL
try:
        r = requests.get(url, stream = True) #DL the URL

        with open("bglug.py", "wb") as Pypdf:
                for chunk in r.iter_content(chunk_size = 1024):

                        if chunk:

                                Pypdf.write(chunk) #write 1KB(?) at a time
except:
	print("There was an ERROR upgrading to the LATEST VERSION. You may have outdated information")
