import requests,json
from testFile.readConfig import ReadConfig as readConfig
from common import common_public
localReadConfig = readConfig()
from common.Log import MyLog as Log
log = Log.get_log()
logging = log.logger






class ConfigHttp:
    def __init__(self):
        global timeout

        timeout = localReadConfig.get_http("timeout")


        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        logging.info('------------------------------start----------------------')
        url1 = common_public.URL() + url
        logging.info('url:' + url1)
        self.url = url1



    def set_headers(self, header):
        self.headers = header


    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        data1 = json.dumps(data)
        logging.info('data:'+data1)
        self.data = data1

    def set_files(self, file):
        self.files = file

    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            response.raise_for_status()
            result = response.json()
            return result
        except TimeoutError:
            logging.error("Time out!")
            return None

    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            response.raise_for_status()
            result = response.json()
            logging.info('result:'+response.text)
            return result
        except TimeoutError:
            logging.error("Time out!")
            return None

if __name__ == '__main__':
    pass