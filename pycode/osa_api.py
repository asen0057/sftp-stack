import requests,os,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ApiWork(object):
    """OSA API function"""
    def __init__(self,data,pid,apikey):
        self.data = {}
        self.pid = ''
        self.apiKey = ''
        self.fileName = 'all.csv'
        self.folder = ''
        self.pidUrl = 'https://osa.okla.seagate.com/API/pids'
        self.insertUrl = 'https://osa.okla.seagate.com/API/'

    def get_job_status(self):
        """
            return job ststus: completed, error, stopped, queue
        """
        statusUrl = ''.join([self.pidUrl, self.pid, '/status?apikey=', self.apiKey])
        job = requests.get(statusUrl, verify=False)
        return job

    def upload_data(self):
        """
            return job 
        """
        uplaodUrl = ''.join([self.pidUrl, self.pid, '/workflowVariables?apikey=', self.apiKey])
        job = requests.put(uplaodUrl, data=self.data, verify=False)
        return job
    
    def get_new_instance(self):
        instanceUrl = ''.join([self.pidUrl, self.pid, '/instantiate?apikey=', self.apiKey)
        job = requests.post(instanceUrl, verify=False)
        if job.json()['success'] == True:
            self.pid = job.json()['data'][1]
        return job
            
    
    def download_data(self):
        """return requests job
        with open(localfile) as f:
            f.write(job.conytent)
        """
        downloadUrl = ''.join([self.pidUrl, self.pid, '/files/', self.fileName, '?apikey=',self.apiKey])
        if self.folder != '':
            downloadUrl = ''.join([downloadUrl, '&filepath=', self.folder])
        job = requests.get(downloadUrl, verify=False)
        return job