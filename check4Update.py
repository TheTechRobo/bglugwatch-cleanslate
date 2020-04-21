import requests, sys, shutil
'''
Source: https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests/39217788#39217788
Thanks for using!
Please add attribution.
'''
def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
            return local_filename
print("Commencing download...")
download_file("https://hello.ca")
print("33% done.", end="\r")
download_file("https://thetechrobo.github.io")
print("66% done.", end="\r")
download_file("link.to/version")
print("Done download!", end="\r")
print()
