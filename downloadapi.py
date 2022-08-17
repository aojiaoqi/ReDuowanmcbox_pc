import os
import api
import urllib.request
T = api.Dot('/ver/download/')
def DownloadVer():
    os.system('del newver.exe')
    urllib.request.urlretrieve(T,'newver.exe')
    os.system('start newver.exe')