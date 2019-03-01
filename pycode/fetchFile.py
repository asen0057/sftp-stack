from pycode.sftpconfig import sftp
import pysftp

class sftpFile(sftp):
    def __init__(self,sftp):
        self.con

conn = pysftp.Connection(host=sftp().host,username=sftp().username,password=sftp().password)