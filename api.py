import urllib3.request
import time
http = '101.43.48.113'
def MakeUrl(api):
    return http + '/api/' + api
def DoT(api):
    get = urllib3.request.urlopen(MakeUrl(api))
    html = get.read().decode('utf-8')
    return html
def __main__():
    print('ReDuowanmcbox Api Core V1.0')
    print('Using: Dot (api)')
    time.sleep(3)
if __name__ == "__main__":
    __main__()
