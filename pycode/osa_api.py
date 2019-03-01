import requests,os,urllib3
urllibe.disable_warnings(urllib3.exceptions.InsecurRequestWarning)

class ApiWork(object):
    def __init__(self,data,pid,apikey):
        self.data = {}
        self.pid = ''
        self.apiKey = ''
        self.pidUrl = 'https://osa.okla.seagate.com/API/pids'
        self.insertUrl = 'https://osa.okla.seagate.com/API/'

    def get_job_status(self):
        statusUrl = ''.join([pidUrl, self.pid, '/status?apikey=', self.apiKey])
        jobStatus = requests.get(statusUrl, verify=False)
        return jobStatus