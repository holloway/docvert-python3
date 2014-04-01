#based on https://github.com/shazow/workerpool/wiki/Mass-Downloader
import os
import urllib.request, urllib.error, urllib.parse
import lib.workerpool

class DownloadUrl(lib.workerpool.Job):
    def __init__(self, url, http_timeout=10):
        self.url = url
        self.http_timeout = http_timeout

    def run(self):
        try:
            self.response = urllib.request.urlopen(self.url, None, self.http_timeout).read()
        except urllib.error.URLError as e:
            self.response = e

def download(urls, workerpool_size=5):
    pool = lib.workerpool.WorkerPool(size=workerpool_size)
    for url in urls:
        pool.put(DownloadUrl(url))
    pool.shutdown()
    pool.wait()
    print(dir(pool))

def demo():
    download([
        'https://github.com/shazow/workerpool/wiki/Mass-Downloader',
        'http://yahoo.com',
        'http://twitter.com/',
        'http://www.google.com/',
        'http://www.stuff.co.nz/',
        'http://trademe.co.nz/',
        'http://av.com/',
        'http://reddit.com/',
        'http://slashdot.org/'
    ])
