# SOURCE: https://likegeeks.com/downloading-files-using-python/
import requests
"""
try:
        r = requests.get(url, stream = True) #DL the URL

        with open("bglug.py", "wb") as Pypdf:
                for chunk in r.iter_content(chunk_size = 1024):

                        if chunk:
                                Pypdf.write(chunk) #write 1KB(?) at a time
"""
url = 'https://thetechrobo.github.io/resources/bglug.py' #url to DL
try: 
    r = requests.get(url).text #download
    #r = r.decode("UTF-8") #change from binary to unicode
    exec(r) #run the code
except ImportError as ename:
	print("There was an ERROR upgrading to the LATEST VERSION (%s). You may have outdated information." % ename)
