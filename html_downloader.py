#html页面下载器
import urllib.request


class HtmlDownloader(object):

    #下载网页的方法
    def download(self, url):
        if url is None:
            return None
        response=urllib.request.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()