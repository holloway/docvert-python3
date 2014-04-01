# Based on code from
# http://stackoverflow.com/questions/257409/download-image-file-from-the-html-page-source-using-python
# but multithreaded, etc.
from BeautifulSoup import BeautifulSoup as bs
import urllib.parse
from urllib.request import urlopen
from urllib.request import urlretrieve
import os
import sys

def get_urls(url, storage, storage_prefix):
    """Downloads all the images at 'url' to /test/"""
    soup = bs(urlopen(url))
    parsed = list(urllib.parse.urlparse(url))

    for image in soup.findAll("img"):
        print("Image: %(src)s" % image)
        filename = image["src"].split("/")[-1]
        parsed[2] = image["src"]
        storage_path = os.path.join(storage_prefix, filename)
        
        url = urllib.parse.urlunparse(parsed)
        if url.lower().startswith("http"):
            url = image["src"]
        data = urllib.request.urlopen(url)
